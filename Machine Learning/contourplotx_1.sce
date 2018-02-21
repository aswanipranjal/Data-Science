function f = quadratic(x)
    f = x(1)**2 + x(2)**2;
endfunction

xdata = linspace(-1, 1, 100);
ydata = linspace(-1, 1, 100);

for i = 1:length(xdata)
    for j = 1:length(ydata)
        x = [xdata(i) ydata(j)];
        zdata(i, j) = quadratic(x);
    end
end

contour(xdata, ydata, zdata, [0.1 0.3 0.5 0.7])
