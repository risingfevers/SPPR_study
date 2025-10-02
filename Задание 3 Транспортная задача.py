from cvxopt.modeling import variable, op
from cvxopt import matrix

x = variable(25, 'x')
c = [3,4,3,1,5,2,3,5,0,8,1,2,3,3,4,4,5,7,9,9,5,6,8,4,7]
z = sum(c[i] * x[i] for i in range(25))

mass1 = (x[0] + x[1] + x[2] + x[3] + x[4] <= 300)
mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= 200)
mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 100)
mass4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= 200)
mass5 = (x[20] + x[21] + x[22] + x[23] + x[24] <= 300)


mass6 = (x[0] + x[5] + x[10] + x[15] + x[20] == 300)
mass7 = (x[1] + x[6] + x[11] + x[16] + x[21] == 200)
mass8 = (x[2] + x[7] + x[12] + x[17] + x[22] == 300)
mass9 = (x[3] + x[8] + x[13] + x[18] + x[23] == 100)
mass10 = (x[4] + x[9] + x[14] + x[19] + x[24] == 400)

# Условие неотрицательности!!!
x_non_negative = (x >= 0)

# Проверка сбалансированности задачи- она не ссбалансирована, будем добавлять фиктивного потавщика
total_supply = 300 + 200 + 100 + 200 + 300  # 1100
total_demand = 300 + 200 + 300 + 100 + 400  # 1300

print(f"Общее предложение: {total_supply}")
print(f"Общий спрос: {total_demand}")

if total_supply < total_demand:
    print("ЗАМЕЧАНИЕ: Задача несбалансированная :/ ! Спрос превышает предложение.")
    # Добавляем фиктивного поставщика
    print("Добавим фиктивного поставика") 
    
    # Переопределяем переменные после добавьения фиктивного поставщика
    x = variable(30, 'x')  # 6×5  = 30 - переменных
    
    # Новые коэффициенты (фиктивные перевозки имеют стоимость 0)
    c_extended = c + [0, 0, 0, 0, 0]
    z = sum(c_extended[i] * x[i] for i in range(30))
    
    # Ограничения по предложению (включая фиктивного поставщика)
    mass1 = (x[0] + x[1] + x[2] + x[3] + x[4] <= 300)
    mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= 200)
    mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 100)
    mass4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= 200)
    mass5 = (x[20] + x[21] + x[22] + x[23] + x[24] <= 300)
    mass_fictive = (x[25] + x[26] + x[27] + x[28] + x[29] <= 200)  # Фиктивный поставщик
    
    # Ограничения по спросу остаются прежними
    mass6 = (x[0] + x[5] + x[10] + x[15] + x[20] + x[25] == 300)
    mass7 = (x[1] + x[6] + x[11] + x[16] + x[21] + x[26] == 200)
    mass8 = (x[2] + x[7] + x[12] + x[17] + x[22] + x[27] == 300)
    mass9 = (x[3] + x[8] + x[13] + x[18] + x[23] + x[28] == 100)
    mass10 = (x[4] + x[9] + x[14] + x[19] + x[24] + x[29] == 400)
    
    x_non_negative = (x >= 0)
    
    problem = op(z, [mass1, mass2, mass3, mass4, mass5, mass_fictive, 
                    mass6, mass7, mass8, mass9, mass10, x_non_negative])
else:
    problem = op(z, [mass1, mass2, mass3, mass4, mass5, 
                    mass6, mass7, mass8, mass9, mass10, x_non_negative])

try:
    problem.solve(solver='glpk')
    
    if problem.status == 'optimal':
        print("Результат:")
        for i in range(len(x.value)):
            if x.value[i] > 1e-6:  # Показываем только ненулевые перевозки
                print(f"x[{i}] = {x.value[i]:.2f}")
        
        print("\nСтоимость доставки:")
        print(f"{problem.objective.value()[0]:.2f}")
        
        # Вывод в виде матрицы 5x5 (или 6x5 для фиктивного случая)
        print("\nМатрица перевозок:")
        n_suppliers = 6 if total_supply < total_demand else 5
        for i in range(n_suppliers):
            row = []
            for j in range(5):
                idx = i * 5 + j
                row.append(f"{x.value[idx]:6.1f}" if idx < len(x.value) else "   -   ")
            print(f"Поставщик {i+1}: {''.join(row)}")
            
    else:
        print(f"Проблема не решена. Статус: {problem.status}")
        
except Exception as e:
    print(f"Ошибка при решении: {e}")
    print("Попробуйте установить solver='mosek' или использовать другую библиотеку")

