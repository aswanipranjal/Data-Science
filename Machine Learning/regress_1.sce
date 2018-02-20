
x = [1.2, 2.5, 4.3, 8.3, 11.6];
y = [6.05, 11.6, 15.8, 21.8, 36.8];
Sx = sum(x);
Sx2 = sum(x^2);
Sy = sum(y);
Sxy = sum(x.*y);
n = length(x);
A = [Sx, n; Sx2, Sx];
B = [Sy; Sxy];
p = A\B
disp(p)

deff('[y]=yh(x)', 'y=p(1).*x+p(2)')
plot2d(x, y, -1, '011', ' ', rect)
xtitle('Simple linear regression', 'x', 'y')
