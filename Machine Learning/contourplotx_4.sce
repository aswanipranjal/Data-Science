function f = quad(x)
    f = x^2
endfunction

function f = quad2(x)
    f = 2 * x^2
endfunction

xdata = linspace(1, 10, 50);
ydata = quad(xdata);
plot(xdata, ydata, '+-')
ydata2 = quad2(xdata);
plot(xdata, ydata2, 'o-')
xtitle('Plot title', 'X-axis', 'Y-axis');
legend('x^2', '2x^2')
