import sympy as sp

# Definisi variabel simbolik
x = sp.symbols('x')

# Soal 1: y = (x^2 - 2x + 5) / (x^2 + 2x - 3)
numerator = x**2 - 2*x + 5
denominator = x**2 + 2*x - 3
y1 = numerator / denominator
y1_derivative = sp.diff(y1, x)
print("Turunan pertama soal 1:", y1_derivative)

# Soal 2: y = (2x - 3)^10
y2 = (2*x - 3)**10
y2_derivative = sp.diff(y2, x)
print("Turunan pertama soal 2:", y2_derivative)

# Soal 3: y = sin^3(x)
y3 = sp.sin(x)**3
y3_derivative = sp.diff(y3, x)
print("Turunan pertama soal 3:", y3_derivative)

# Soal 4: y = cos^4(4x^2 - x)
y4 = sp.cos(4*x**2 - x)**4
y4_derivative = sp.diff(y4, x)
print("Turunan pertama soal 4:", y4_derivative)

# Soal 5: y = [(x + 1) / (x - 1)]^2
fraction = (x + 1) / (x - 1)
y5 = fraction**2
y5_derivative = sp.diff(y5, x)
print("Turunan pertama soal 5:", y5_derivative)

# Soal 6: y = sin(x) * tan(x^2 + 1)
y6 = sp.sin(x) * sp.tan(x**2 + 1)
y6_derivative = sp.diff(y6, x)
print("Turunan pertama soal 6:", y6_derivative)