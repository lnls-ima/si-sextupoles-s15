function opt = get_params()
    ring0 = sirius_si_lattice();
    
    params.ring0 = ring0;
    params.twi0 = calctwiss(params.ring0);
    params.nus = [params.twi0.mux(end)/2/pi, params.twi0.muy(end)/2/pi];

    params.data = specifics.load_data();
    
    params.fam_data = sirius_si_family_data(params.ring0);
    params.fam_sizes = zeros(length(params.data.families), 1);
    for i=1:length(params.data.families)
        fam = params.data.families{i};
        params.fam_sizes(i) = size(params.fam_data.(fam).ATIndex, 1);
    end
    params.fam_idcs = [0; cumsum(params.fam_sizes)];
    
    orbit.bpm_idx = params.fam_data.BPM.ATIndex(:);
    orbit.hcm_idx = params.fam_data.CH.ATIndex(:);
    orbit.vcm_idx = params.fam_data.CV.ATIndex(:);
    orbit.max_nr_iter = 20;
    orbit.svs = 'all';
    r = calc_respm_cod(params.ring0, orbit.bpm_idx, orbit.hcm_idx, orbit.vcm_idx);
    orbit.respm = r.respm;
    params.orbit = orbit;
    
    opt.objective_fun = @specifics.calc_residue;
    opt.objective_data = params;
    opt.small_change = @specifics.change_order;
    opt.random_change = @specifics.permute_randomly;
    opt.Nid = 5000;
    opt.Ncut = 1;
    opt.NG = 400;
    opt.Nobj = 2;
    opt.config0 = (1:length(params.data.names))';
    opt.folder = 'run04';
    opt.continue = true;
    opt.arbitrary_initial = false;
    opt.print_info = @specifics.print_info;
    opt.simulanneal_Niter = 100000;
    opt.simulanneal_weight = [30, 50];
end