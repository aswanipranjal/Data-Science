function f = quadratic(x)
    f = x.^2
endfunction

xdata = linspace(1, 10, 50);
ydata = quadratic(xdata);
plot(xdata, ydata)
title('Random title')
