function ring = insert_mags(ring, params, idcs)
    data = params.data;
    monob = data.monomialsb;
    monoa = data.monomialsa;
    main_mono = 3;
    for i=1:length(data.families)
        fam = data.families{i};
        cur = data.currents{i};
        idx = idcs((params.fam_idcs(i)+1):params.fam_idcs(i+1));
        ave_exc = mean(data.(cur).polB(idx, main_mono)) - 1;
        data.(cur).polB(idx, main_mono) = data.(cur).polB(idx, main_mono) - ave_exc;
        for jj=1:length(idx)
            idc = idx(jj);
            for kk=1:size(params.fam_data.(fam).ATIndex, 2)
                ind = params.fam_data.(fam).ATIndex(jj, kk);
                k_old = ring{ind}.PolynomB(main_mono);
                ring{ind}.PolynomB(monob) = data.(cur).polB(idc, monob) * k_old;
                ring{ind}.PolynomA(monoa) = data.(cur).polA(idc, monoa) * k_old;
            end
        end
    end
end