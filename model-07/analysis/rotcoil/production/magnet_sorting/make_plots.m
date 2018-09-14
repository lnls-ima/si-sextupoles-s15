function twi = make_plots(indcs, params)
   
%     rings = create_rings(indcs, params.data);
% 
%     fs = fieldnames(rings);
%     for i=1:length(fs)
%         m = fs{i};
%         twi.(m) = calctwiss(rings.(m), 'N+1');
%         coup.(m) = lnls_calc_coupling(rings.(m));
%     end
%     %%
%     figure('Position', [100, 10, 1200, 2000]);
%     axs(1) = subplottight(5, 1, 1, 'left', 0.1, 'vspace', 0.06);
%     axs(2) = subplottight(5, 1, 2, 'left', 0.1, 'vspace', 0.06);
%     axs(3) = subplottight(5, 1, 3, 'left', 0.1, 'vspace', 0.06);
%     axs(4) = subplottight(5, 1, 4, 'left', 0.1, 'vspace', 0.06);
%     axs(5) = subplottight(5, 1, 5, 'left', 0.1, 'vspace', 0.06);
%     for i=1:length(axs)
%         ax = axs(i);
%         set(ax, 'Box', 'on', 'FontSize', 16, ...
%                 'XGrid', 'on', 'YGrid', 'on', 'NextPlot', 'add');
%         xlabel(ax, 'position [m]', 'FontSize', 16);
%     end
% 
%     for i=1:length(fs)
%         m = fs{i};
%         tw = twi.(m);
%         plot(axs(1), tw.pos, tw.cox*1000, 'LineWidth', 3);
%         plot(axs(2), tw.pos, tw.coy*1000, 'LineWidth', 3);
%         plot(axs(3), tw.pos, 100*(tw.betax-twi.bare.betax)./twi.bare.betax, 'LineWidth', 3);
%         plot(axs(4), tw.pos, 100*(tw.betay-twi.bare.betay)./twi.bare.betay, 'LineWidth', 3);
%         plot(axs(5), tw.pos, coup.(m).tilt*180/pi, 'LineWidth', 3);
%     end
% 
%     ylabel(axs(1), 'Horizontal Orbit [mm]');
%     ylabel(axs(2), 'Vertical Orbit [mm]');
%     ylabel(axs(3), 'Horizontal beta beat [%]');
%     ylabel(axs(4), 'Vertical beta beat [%]');
%     ylabel(axs(5), 'Tilt Angle [°]');
% 
%     legend(axs(2), 'best', fs);

    
    figure('Position', [100, 10, 1200, 2000]);
    axs(1) = subplottight(4, 1, 1, 'left', 0.1, 'vspace', 0.06);
    axs(2) = subplottight(4, 1, 2, 'left', 0.1, 'vspace', 0.06);
    axs(3) = subplottight(4, 1, 3, 'left', 0.1, 'vspace', 0.06);
    axs(4) = subplottight(4, 1, 4, 'left', 0.1, 'vspace', 0.06);
    for i=1:length(axs)
        ax = axs(i);
        set(ax, 'Box', 'on', 'FontSize', 16, ...
            'XGrid', 'on', 'YGrid', 'on', 'NextPlot', 'add');
        xlabel(ax, 'position [m]', 'FontSize', 16);
    end
    
    fs = fieldnames(indcs);
    n = length(params.data.families);
    for ii=1:length(fs)
        id = indcs.(fs{ii});
        exc = zeros(params.data.num_used_mags, 1);
        roll = zeros(params.data.num_used_mags, 1);
        x0 = zeros(params.data.num_used_mags, 1);
        y0 = zeros(params.data.num_used_mags, 1);
        for i=1:n
            cur = params.data.currents{i};
            idcs = (params.fam_idcs(i)+1):params.fam_idcs(i+1);
            exc(idcs) = params.data.(cur).exc_err(id(idcs));
            roll(idcs) = params.data.(cur).roll(id(idcs));
            x0(idcs) = params.data.(cur).x0(id(idcs));
            y0(idcs) = params.data.(cur).y0(id(idcs));
        end
        plot(axs(1), exc*100, '.-', 'MarkerSize', 20);
        plot(axs(2), roll*1000, '.-', 'MarkerSize', 20);
        plot(axs(3), x0*1e6, '.-', 'MarkerSize', 20);
        plot(axs(4), y0*1e6, '.-', 'MarkerSize', 20);
    end
 
    ylabel(axs(1), 'Excitation Error [%]');
    ylabel(axs(2), 'Roll Error [mrad]');
    ylabel(axs(3), 'x_0 [urad]');
    ylabel(axs(4), 'y_0 [urad]');

    legend(axs(2), 'best', fs);
    
    for j=1:length(axs)
        yl = get(axs(j), 'YLim');
        for i=1:n
            plot(axs(j), params.fam_idcs(i+1)*[1,1]+0.2, yl, '-k', 'LineWidth', 2);
        end
    end
end