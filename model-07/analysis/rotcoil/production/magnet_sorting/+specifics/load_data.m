function data = load_data()
    % indices to discard. Based on sorting of excitation errors at I=50A;
    % Discard the first 2 with lower and the last 6 with higher exc_err;
%     idcs = [71, 1, 65, 63, 29, 77, 4, 40];
%     idcs = setdiff(1:78, idcs);

    files = regexp(ls('../'), 'MULTIPOLES-FAM1-([0-9]{1,3})A\.txt', 'tokens');
    c = zeros(length(files), 1);
    for i=1:length(files)
        c(i) = str2double(files{i}{1});
    end
    c = sort(c);
    for i=1:length(c)
        st = sprintf('I%03d', c(i));
        [data.(st), names] = import_readme(c(i));
    end
    data.names = names;
    data.families = {...
        'SDA0', 'SFA0', 'SDB0', 'SFB0', 'SDP0', 'SFP0', ...
        'SDA1', 'SFA1', 'SDB1', 'SFB1', 'SDP1', 'SFP1', ...
        'SDA2', 'SFA2', 'SDB2', 'SFB2', 'SDP2', 'SFP2', ...
        'SDA3', 'SDB3', 'SDP3'};
    data.currents = {...
        'I050', 'I030', 'I050', 'I050', 'I050', 'I050', ...
        'I110', 'I130', 'I090', 'I150', 'I090', 'I150', ...
        'I050', 'I110', 'I090', 'I130', 'I090', 'I130', ...
        'I090', 'I110', 'I110'};

%     % Test the results with currents near the one used for optimizations.
%     data.currents = {...
%         'I070', 'I050', 'I070', 'I070', 'I070', 'I070', ...
%         'I130', 'I150', 'I110', 'I168', 'I110', 'I168', ...
%         'I070', 'I130', 'I110', 'I150', 'I110', 'I150', ...
%         'I110', 'I130', 'I130'};
%     data.currents = {...
%         'I030', 'I010', 'I030', 'I030', 'I030', 'I030', ...
%         'I090', 'I110', 'I070', 'I130', 'I070', 'I130', ...
%         'I030', 'I090', 'I070', 'I110', 'I070', 'I110', ...
%         'I070', 'I090', 'I090'};
    data.num_used_mags = 280;
    data.monomialsb = 3; %[1, 2, 3];
    data.monomialsa = 3; %[1, 2, 3];
    data.main_monomial = 3;
end

function [data, names] = import_readme(cur, ind)
    dataArray1 = read_file(sprintf('../MULTIPOLES-FAM1-%dA.txt', cur));
    dataArray2 = read_file(sprintf('../MULTIPOLES-FAM2-%dA.txt', cur));

    names = [dataArray1{1}; dataArray2{1}];
    data.current = [dataArray1{2}; dataArray2{2}];
    pols1 = cell2mat(dataArray1(3:end-1));
    pols2 = cell2mat(dataArray2(3:end-1));
    pols = [pols1; pols2];
    
    if exist('ind', 'var')
        names = names(ind, :);
        data.current = data.current(ind, :);
        pols = pols(ind, :);
    end
    
    ave_kl = mean(pols(:, 3));
    data.polB = pols(:, 1:15) / ave_kl;
    data.polA = pols(:, 16:end) / ave_kl;
    data.exc_err = data.polB(:, 3) - 1;
    data.roll = atan(data.polA(:, 3)./data.polB(:, 3)) / 3;
    z0 = -(data.polB(:, 2) + 1i * data.polA(:, 2)) ./ (data.polB(:, 3) + 1i * data.polA(:, 3)) / 2;
    data.x0 = real(z0);
    data.y0 = imag(z0);
end

function dataArray = read_file(filename)
    % Initialize variables.
    delimiter = {' '};
    startRow = 4;
    endRow = inf;
    
    % Format for each line of text:
    % For more information, see the TEXTSCAN documentation.
    formatSpec = ['%s', repmat('%f',1,31), '%[^\n\r]'];

    % Open the text file.
    fileID = fopen(filename,'r');

    % Read columns of data according to the format.
    % This call is based on the structure of the file used to generate this
    % code. If an error occurs for a different file, try regenerating the code
    % from the Import Tool.
    dataArray = textscan(...
        fileID, formatSpec, endRow(1)-startRow(1)+1,...
        'Delimiter', delimiter, 'MultipleDelimsAsOne', true,...
        'HeaderLines', startRow(1)-1, 'ReturnOnError', false,...
        'EndOfLine', '\r\n');
    
    % Close the text file.
    fclose(fileID);
end