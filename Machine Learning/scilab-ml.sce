t = csvRead('sce_data_classification.csv')

t0 = t(find(t(:, $)==0), :);
t1 = t(find(t(:, $)==1), :);

clf(0);
scf(0);

plot(t0(:, 1), t0(:, 2), 'bo')
plot(t1(:, 1), t0(:, 2), 'rx')