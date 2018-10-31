function create_sorting_table(indcs, params)
    section.SFA0 = {'01', '05', '09', '13', '17'};
    section.SFP0 = {'03', '07', '11', '15', '19'};
    section.SFB0 = arrayfun(@(x) sprintf('%02d',x), 2:2:20, 'UniformOutput', false);
    section.SFA1 = section.SFA0;
    section.SFP1 = section.SFP0;
    section.SFB1 = section.SFB0;
    section.SFA2 = section.SFA0;
    section.SFP2 = section.SFP0;
    section.SFB2 = section.SFB0;
    section.SDA0 = section.SFA0;
    section.SDP0 = section.SFP0;
    section.SDB0 = section.SFB0;
    section.SDA1 = section.SFA0;
    section.SDP1 = section.SFP0;
    section.SDB1 = section.SFB0;
    section.SDA2 = section.SFA0;
    section.SDP2 = section.SFP0;
    section.SDB2 = section.SFB0;
    section.SDA3 = section.SFA0;
    section.SDP3 = section.SFP0;
    section.SDB3 = section.SFB0;
    
    subsection.SFA0 = {'M1', 'M2'};
    subsection.SFP0 = subsection.SFA0;
    subsection.SFB0 = subsection.SFA0;
    subsection.SDA0 = subsection.SFA0;
    subsection.SDP0 = subsection.SFA0;
    subsection.SDB0 = subsection.SFA0;
    subsection.SFA1 = {'C1', 'C4'};
    subsection.SFP1 = subsection.SFA1;
    subsection.SFB1 = subsection.SFA1;
    subsection.SDA1 = subsection.SFA1;
    subsection.SDP1 = subsection.SFA1;
    subsection.SDB1 = subsection.SFA1;
    subsection.SDA2 = subsection.SFA1;
    subsection.SDP2 = subsection.SFA1;
    subsection.SDB2 = subsection.SFA1;
    subsection.SFA2 = {'C2', 'C3'};
    subsection.SFP2 = subsection.SFA2;
    subsection.SFB2 = subsection.SFA2;
    subsection.SDA3 = subsection.SFA2;
    subsection.SDP3 = subsection.SFA2;
    subsection.SDB3 = subsection.SFA2;

    alin = @(x,y) strjust(sprintf(x, y), 'center');
    
    mag_names = struct();
    fs = fieldnames(section);
    fun = @(y1, y2) any(cellfun(@(x) strcmp(x, y1), y2));
    for i=1:length(fs)
        fam = fs{i};
        sec = section.(fam);
        ssec = subsection.(fam);
        n = length(sec)*length(ssec);
        c = cell(n, 1);
        for j=1:n
            si = floor((j-1)/length(ssec)) + 1;
            ssi = mod(j-1, length(ssec)) + 1;
            c{j} = sprintf('SI-%s%s:MA-%s', sec{si}, ssec{ssi}, fam);
        end
        if fun('M1', ssec) && fun('01', sec)
            c = circshift(c, [-1,0]);
        end
        mag_names.(fam) = c;
    end

    scope = [...
        '| scope="col" width="200px" style="font-weight:bold; text-align:center;" | Magnet Name\n', ...
        '| scope="col" width="200px" style="font-weight:bold; text-align:center;" | Magnet Serial ID\n', ...
        '|-\n'];
    headerfam = '! colspan="2" style="font-weight:bold; font-size:24px; text-align:center;" | %s \n|-\n';
    line = [...
        '| style="text-align:center; background-color: %s;" | %s\n', ...
        '| style="text-align:center; background-color: %s;" | %s\n', ...
        '|-\n'];
    final = '|}\n</figtable>\n';
    cs = {'#D1D1D1', '#F1F1F1'};
    
    fi = fopen('sorting_table.txt', 'w');
    fprintf(fi, '<!-- The order used was the result G391I180 of optimization run04. -->\n');
    fprintf(fi, '<!-- Results can be found in data repository of si-sextupoles-s15 inside the folder: -->\n');
    fprintf(fi, '<!--     model-07/analysis/rotcoil/production/magnet_sorting -->\n\n');
    fprintf(fi, '<figtable id="tab:si_sextupoles_s15_installation">\n');
    fprintf(fi, '{|  {{SiriusTable}}\n|+ <caption>Storage Ring Sextupoles Installation.</caption>\n');
    for i=1:length(params.data.families)
        fam = params.data.families{i};
        fprintf(fi, headerfam, fam);
        fprintf(fi, scope);
        idx = indcs((params.fam_idcs(i)+1):params.fam_idcs(i+1));
        for jj=1:length(idx)
            mag_name = mag_names.(fam){jj};
            c = cs{mod(jj-1, 2) + 1};
            fprintf(fi, line, c, mag_name, c, params.data.names{idx(jj)});
        end
    end
    idx = indcs((params.fam_idcs(end)+1):end);
    fprintf(fi, headerfam, 'Not Used');
    fprintf(fi, scope);
    for jj=1:length(idx)
        c = cs{mod(jj-1, 2) + 1};
        fprintf(fi, line, c, '---', c, params.data.names{idx(jj)});
    end
    fprintf(fi, final);
    fprintf(fi, '\n\n');
    fclose(fi);
end