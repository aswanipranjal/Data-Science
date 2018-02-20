// simulation of data for a(3, 5) and b(3, 1)
x = rand(5, 100);
aa = testmatrix('magi', 5);
aa = aa(1:3, :);
bb = [9; 10; 11];
y = aa * x + bb * ones(1, 100) + 0.1 * rand(3, 100);

// Identification
[a, b, sig] = reglin(x, y);
max(abs(aa - a))
max(abs(bb - b))

// Another example: fitting a polynomial
f = 1:100;
x = [f.*f; f];
y = [2 3]*x + 10*ones(f) + 0.1*rand(f);
[a, b] = reglin(x, y)

// Generating an odd function
x = -30:30;
y = x.^3;

// Extracting the least square mean of that function
[a, b] = reglin(x, y);
plot(x, y, 'red')
plot(x, a*x+b)
