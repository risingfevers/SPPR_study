from scipy.optimize import linprog
import numpy as np

supply = [300, 200, 100, 200, 300]
demand = [300, 200, 300, 100, 400]

costs = [
    [3, 4, 3, 1, 5],
    [2, 3, 5, 0, 8], 
    [1, 2, 3, 3, 4],
    [4, 5, 7, 9, 9],
    [5, 6, 8, 4, 7]
]

c = np.array(costs).flatten()

a_ub = []
b_ub = []

for i in range(5):
    row = [0] * 25
    for j in range(5):
        row[i * 5 + j] = 1
    a_ub.append(row)
    b_ub.append(supply[i])

a_eq = []
b_eq = []

for j in range(5):
    row = [0] * 25
    for i in range(5):
        row[i * 5 + j] = 1
    a_eq.append(row)
    b_eq.append(demand[j])

result = linprog(c, A_ub=a_ub, b_ub=b_ub, A_eq=a_eq, b_eq=b_eq, method='highs')

print("Статус:", result.message)
print("Минимальная стоимость:", result.fun)

print("\nОптимальный план:")
x_optimal = result.x.reshape(5, 5)
for i in range(5):
    print(f"A{i+1}: ", end="")
    for j in range(5):
        if x_optimal[i, j] > 1e-6:
            print(f"→B{j+1}:{x_optimal[i, j]:.0f}  ", end="")
    print()

print("\nМатрица перевозок:")
print(x_optimal.round().astype(int))
