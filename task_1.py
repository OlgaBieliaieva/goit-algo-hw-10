from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="production-optimization", sense=LpMaximize)

# Змінні: кількість вироблених лимонаду (L) і фруктового соку (F)
L = LpVariable(name="Lemonade", lowBound=0, cat='Integer')
F = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')

# Цільова функція: максимізуємо кількість вироблених напоїв
model += L + F, "Total Production"

# Обмеження на ресурси
model += (2 * L + 1 * F <= 100), "Water Constraint"
model += (1 * L <= 50), "Sugar Constraint"
model += (1 * L <= 30), "Lemon Juice Constraint"
model += (2 * F <= 40), "Fruit Puree Constraint"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Optimal number of Lemonade units: {L.varValue}")
print(f"Optimal number of Fruit Juice units: {F.varValue}")