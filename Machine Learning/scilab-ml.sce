t = csvRead('sce_data_classification.csv')
P = t(:, 1:2)';
T = t(:, 3)';
plot_2group(P, T);
