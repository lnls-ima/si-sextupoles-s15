function plot_sorted(data)
    cur = {
%         'I002', 'I004', 'I006', 'I008', 'I010', 'I030', ...
        'I050', 'I070', 'I090', 'I110', 'I130', 'I150', 'I168'};
    params = {'x0', 'y0', 'exc_err', 'roll'};
    coefs = [1e6, 1e6, 100, 1e3];
    labs = {' [um]', ' [um]', ' [%]', ' [mrad]'};
    figure('Position', [100, 10, 3200, 2000]);
    axs(1) = subplot(4, 1, 1);
    axs(2) = subplot(4, 1, 2);
    axs(3) = subplot(4, 1, 3);
    axs(4) = subplot(4, 1, 4);
    for i=1:length(params)
        ax = axs(i);
        set(ax, 'Box', 'on', 'FontSize', 16, ...
                'XGrid', 'on', 'YGrid', 'on', 'NextPlot', 'add');
        xlabel(ax, 'index', 'FontSize', 16);
        ylabel(ax, [params{i}, labs{i}], 'FontSize', 16);
%         [~, ind] = sort(data.I050.(params{i}));
        ind = 1:length(data.I050.exc_err);
        for j=1:length(cur)
            plot(ax, coefs(i)*data.(cur{j}).(params{i})(ind), 'o-', 'MarkerSize', 10, 'LineWidth', 3);
        end
    end
end