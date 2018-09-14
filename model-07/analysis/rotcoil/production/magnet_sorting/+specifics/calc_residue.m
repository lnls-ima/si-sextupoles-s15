function res = calc_residue(indcs, params)
%% RING MODEL BASED RESIDUE
%     ring = specifics.insert_mags(params.ring0, params.data, params.fam_data, indcs);
% 
%     [TD, ~] = twissring(ring, 0, 1:length(ring));
% 
%     beta = cat(1, TD.beta);
%     tw.betax = beta(:,1);
%     tw.betay = beta(:,2);
% %     co = cat(1,TD.ClosedOrbit);
% %     tw.cox  = co(1:4:end);
% %     tw.coy  = co(3:4:end);
%     
%     bbx = (tw.betax-params.twi0.betax)./params.twi0.betax;
%     rmsx = sqrt(trapz(params.twi0.pos, bbx.*bbx)/params.twi0.pos(end));
%     bby = (tw.betay-params.twi0.betay)./params.twi0.betay;
%     rmsy = sqrt(trapz(params.twi0.pos, bby.*bby)/params.twi0.pos(end));
% 
%     coup = lnls_calc_coupling(ring);
%     
%     res(1) = rmsx * 100;
%     res(2) = rmsy * 100;
%     res(3) = coup.emit_ratio * 100;
%     
%% STRENGTH BASED RESIDUE
    n = length(params.data.families);
    exc = zeros(n, 1);
    roll = zeros(n, 1);
    start = 0;
    for i=1:n
        fam = params.data.families{i};
        cur = params.data.currents{i};
        idx = params.fam_data.(fam).ATIndex;
        sz = size(idx, 1);
        idcs = start + (1:sz);
        start = start + sz;
        exc(i) = std(params.data.(cur).exc_err(indcs(idcs)));
        roll(i) = std(params.data.(cur).roll(indcs(idcs)));
    end
    
    res(1) = rms(exc)*100;
    res(2) = rms(roll)*1000;

end