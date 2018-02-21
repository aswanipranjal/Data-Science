function f = quadratic2(x1, x2)
    f = x1**2 + x2**2
endfunction

xdata = linspace(-1, 1, 100);
ydata = linspace(-1, 1, 100);
contour(xdata, ydata, quadratic2, 10)
