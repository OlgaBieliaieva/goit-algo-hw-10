import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції, яку інтегруємо
def f(x):
    return x ** 2  # Функція y = x^2

# Межі інтегрування
a, b = 0, 2  # Інтегруємо від 0 до 2

# Метод Монте-Карло
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)  # Генеруємо випадкові x у межах [a, b]
y_random = np.random.uniform(0, f(b), N)  # Генеруємо випадкові y у межах [0, f(b)]

# Визначаємо, скільки точок лежить під кривою y = x^2
under_curve = y_random < f(x_random)

# Обчислення інтегралу методом Монте-Карло
# Площа прямокутника: (b - a) * f(b)
# Частка точок під кривою визначає частку площі
integral_mc = (b - a) * f(b) * np.sum(under_curve) / N

# Обчислення інтегралу аналітично за допомогою quad
integral_quad, error = spi.quad(f, a, b)

# Візуалізація результатів
x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, 'r', linewidth=2, label='y = x^2')  # Графік функції
ax.fill_between(x_vals, y_vals, color='gray', alpha=0.3, label='Площа під кривою')  # Заповнюємо площу
ax.scatter(x_random, y_random, c=under_curve, cmap='coolwarm', alpha=0.3, s=1)  # Точки Монте-Карло
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Метод Монте-Карло vs Quad")
ax.legend()
plt.show()

# Виведення результатів
print(f"Інтеграл методом Монте-Карло: {integral_mc}")
print(f"Інтеграл методом quad: {integral_quad}, похибка: {error}")