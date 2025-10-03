from cvxopt.modeling import variable, op
import time
start = time.time()
x = variable(30, 'x')
c= [3,4,3,1,5,2,3,5,0,8,1,2,3,3,4,4,5,7,9,9,5,6,8,4,7, 0, 0, 0, 0, 0]
z=(c[0]*x[0] + c[1]*x[1] +c[2]* x[2] +c[3]*x[3] + c[4]*x[4] +c[5]* x[5]+c[6]*x[6] +c[7]*x[7] +c[8]* x[8]+c[9]*x[9] + c[10]*x[10] +c[11]* x[11] +c[12]*x[12] + c[13]*x[13] +c[14]* x[14]+c[15]*x[15] +c[16]*x[16] +c[17]* x[17] + c[18]*x[18] +c[19]* x[19]+c[20]*x[20] +c[21]*x[21] +c[22]* x[22]+c[23]*x[23] +c[24]*x[24] +c[25]*x[25] +c[26]*x[26] +c[27]*x[27] +c[28]*x[28] +c[29]*x[29])
mass1 = (x[0] + x[1] + x[2] + x[3] + x[4] <= 300)
mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= 200)
mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 100)
mass4 = (x[15] + x[16] + x[17] + x[18] + x[19] <= 200)
mass5 = (x[20] + x[21] + x[22] + x[23] + x[24] <= 300)
massF = (x[25] + x[26] + x[27] + x[28] + x[29] <= 200)

mass6  = (x[0] + x[5] + x[10] + x[15] + x[20] + x[25] == 300)
mass7  = (x[1] + x[6] + x[11] + x[16] + x[21] + x[26] == 200)
mass8  = (x[2] + x[7] + x[12] + x[17] + x[22] + x[27] == 300)
mass9  = (x[3] + x[8] + x[13] + x[18] + x[23] + x[28] == 100)
mass10 = (x[4] + x[9] + x[14] + x[19] + x[24] + x[29] == 400)
massF = (x[25] + x[26] + x[27] + x[28] + x[29] <= 200)
x_non_negative = (x >= 0)
problem =op(z,[mass1,mass2,mass3,mass4 ,mass5,massF, mass6, mass7, mass8, mass9, mass10,x_non_negative])
problem.solve()

print("Статус решения:", problem.status)

if problem.status == 'optimal':
    print("Результат Xopt:")
    x_values = x.value
    for i in range(30):
        print(f"x[{i}] = {x_values[i]}")
    
    print("Минимальная стоимость перевозки:")
    print(problem.objective.value()[0])
else:
    print("Решение не найдено. Статус:", problem.status)

stop = time.time()
print("Время:", stop - start)
