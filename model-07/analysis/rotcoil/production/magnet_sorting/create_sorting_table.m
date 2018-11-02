function create_sorting_table(indcs, params)
    section.SFA0 = {'01', '05', '05', '09', '09', '13', '13', '17', '17', '01'};
    section.SFP0 = {'03', '07', '11', '15', '19'};
    section.SFB0 = arrayfun(@(x) sprintf('%02d',x), 2:2:20, 'UniformOutput', false);
    section.SFP0 = sort([section.SFP0, section.SFP0]);
    section.SFB0 = sort([section.SFB0, section.SFB0]);
    section.SDA0 = section.SFA0;
    section.SDP0 = section.SFP0;
    section.SDB0 = section.SFB0;
    section.SFA1 = {'01', '04', '05', '08', '09', '12', '13', '16', '17', '20'};
    section.SFP1 = {'02', '03', '06', '07', '10', '11', '14', '15', '18', '19'};
    section.SFB1 = arrayfun(@(x) sprintf('%02d',x), 1:20, 'UniformOutput', false);
    section.SFA2 = section.SFA1;
    section.SFP2 = section.SFP1;
    section.SFB2 = section.SFB1;
    section.SDA1 = section.SFA1;
    section.SDP1 = section.SFP1;
    section.SDB1 = section.SFB1;
    section.SDA2 = section.SFA1;
    section.SDP2 = section.SFP1;
    section.SDB2 = section.SFB1;
    section.SDA3 = section.SFA1;
    section.SDP3 = section.SFP1;
    section.SDB3 = section.SFB1;
    
    subsection.SFA0 = {'M2', 'M1'};
    subsection.SDA0 = subsection.SFA0;
    subsection.SFP0 = {'M1', 'M2'};
    subsection.SDP0 = subsection.SFP0;
    subsection.SFB0 = subsection.SFP0;
    subsection.SDB0 = subsection.SFP0;
    subsection.SFA1 = {'C1', 'C4'};
    subsection.SDA1 = subsection.SFA1;
    subsection.SDA2 = subsection.SFA1;
    subsection.SFA2 = {'C2', 'C3'};
    subsection.SDA3 = subsection.SFA2;
    subsection.SFB1 = {'C4', 'C1'};
    subsection.SDB1 = subsection.SFB1;
    subsection.SDB2 = subsection.SFB1;
    subsection.SFB2 = {'C3', 'C2'};
    subsection.SDB3 = subsection.SFB2;
    subsection.SFP1 = subsection.SFB1;
    subsection.SDP1 = subsection.SFB1;
    subsection.SDP2 = subsection.SFB1;
    subsection.SFP2 = subsection.SFB2;
    subsection.SDP3 = subsection.SFB2;

    mag_names = struct();
    fs = fieldnames(section);
    fun = @(y1, y2) any(cellfun(@(x) strcmp(x, y1), y2));
    for i=1:length(fs)
        fam = fs{i};
        sec = section.(fam);
        ssec = subsection.(fam);
        n = length(sec);
        c = cell(n, 1);
        for j=1:n
            ssi = mod(j-1, length(ssec)) + 1;
            c{j} = sprintf('SI-%s%s:MA-%s', sec{j}, ssec{ssi}, fam);
        end
        mag_names.(fam) = c;
    end
    
    create_wiki_table(mag_names, indcs, params);
    create_excel_table(mag_names, indcs, params);
end
    
function create_wiki_table(mag_names, indcs, params)
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

function create_excel_table(mag_names, indcs, params)
    fi = fopen('sorting_excel_table.txt', 'w');
    line = 'Sextupole %12.3f %10s %20s %10s\n';
    spos = findspos(params.ring0, 1:length(params.ring0));
    for i=1:length(params.data.families)
        fam = params.data.families{i};
        ridx = params.fam_data.(fam).ATIndex;
        idx = indcs((params.fam_idcs(i)+1):params.fam_idcs(i+1));
        for jj=1:length(idx)
            pos = ( spos(ridx(jj,1)) + spos(ridx(jj,end)) ) / 2;
            mag_name = mag_names.(fam){jj};
            serial = params.data.names{idx(jj)};
            fprintf(fi, line, pos, fam, mag_name, serial);
        end
    end
    idx = indcs((params.fam_idcs(end)+1):end);
    for jj=1:length(idx)
        fprintf(fi, line, 1000, 'NotUsed', '---', params.data.names{idx(jj)});
    end
    fclose(fi);
end