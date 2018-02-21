function f = quadratic1arg(x)
    f = x(1)**2 + x(2)**2
endfunction

function f = quadratic3(x1, x2)
    f = quadratic1arg([x1 x2])
endfunction

xdata = linspace(-1, 1, 100);
ydata = linspace(-1, 1, 100);
contour(xdata, ydata, quadratic3, [0.1 0.3 0.5 0.7])
