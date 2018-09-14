function idcs = change_order(idcs, params)
    prm = randperm(length(params.data.names), 2);
    
    % to deal with cases where both indices are not used (~1% for Q14)
    if all(prm > params.data.num_used_mags)
        idcs = specifics.change_order(idcs, params);
        return;
    end
    % to deal with cases where indcs exchange between the same family.
    % allowing that would lead to same objectives (see calc_residue).
    if ~any(xor(prm(1) <= params.fam_idcs(2:end), prm(2) <= params.fam_idcs(2:end)))
        idcs = specifics.change_order(idcs, params);
        return;
    end
    
    idcs(prm) = idcs(fliplr(prm));
end