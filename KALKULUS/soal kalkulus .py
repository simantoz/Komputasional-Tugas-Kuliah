import sympy as sp

# Definisikan simbol untuk x dan h
x, h = sp.symbols('x h')

# a. f(x) = 2x + 1
f1 = 2*x + 1

# b. f(x) = x^2 + x
f2 = x**2 + x

# c. f(x) = 2024 (konstan) - gunakan ekspresi simbolik untuk konstan
f3 = sp.Integer(2024)

# Fungsi untuk menghitung turunan menggunakan definisi limit
def derivative(f, x, h):
    return sp.limit((f.subs(x, x + h) - f) / h, h, 0)

# Hitung turunan untuk masing-masing fungsi
f1_derivative = derivative(f1, x, h)
f2_derivative = derivative(f2, x, h)
f3_derivative = derivative(f3, x, h)

# Print hasil turunan
print(f"Turunan dari f(x) = 2x + 1 adalah: {f1_derivative}")
print(f"Turunan dari f(x) = x^2 + x adalah: {f2_derivative}")
print(f"Turunan dari f(x) = 2024 adalah: {f3_derivative}")