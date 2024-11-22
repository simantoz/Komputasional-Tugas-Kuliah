import sympy as sp

# Definisi simbol
x = sp.symbols('x')

# Soal 1
# 1. f(x) = 1 / (x + 1), cari f'(2)
f1 = 1 / (x + 1)
c1 = 2  # Nilai c
f1_prime_c1 = sp.limit((f1 - f1.subs(x, c1)) / (x - c1), x, c1)

# 2. f(x) = x^2 - 4x + 3, cari f'(2)
f2 = x**2 - 4*x + 3
c2 = 2  # Nilai c
f2_prime_c2 = sp.limit((f2 - f2.subs(x, c2)) / (x - c2), x, c2)

# Output hasil
print("Hasil Soal 1:")
print(f"1. f'(2) untuk f(x) = 1 / (x + 1): {f1_prime_c1}")
print(f"2. f'(2) untuk f(x) = x^2 - 4x + 3: {f2_prime_c2}")