# ЭТО ВЕРСИЯ ИДЕТ В ДОПОЛНЕНИЕ К "Задание 2 Матрица" ЧТОБЫ ПОКАЗАТЬ РАЗНИЦУ В ВЫВОДАХ
import numpy as np

matrix  = np.array([[ 5,9,7,7,8],[ 5,5,7,0,2],[12,8,10,6,11],[11,8,2,12,10],[8,7,0,4,10]])
q=[0.0, 0.0, 0.43, 0.57, 0.0]
p=[0.0, 0.0, 0.71, 0.29, 0.0]
answer = {}

lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in np.rot90(matrix)]) # Тут ничего не изменял
print(lower_price, upper_price)
if lower_price==upper_price:print("седловая точка есть", f"ответ v={lower_price}")
else:
  buff=0
  for i,pin in zip(matrix,p):
    buff+=pin*sum([x*y for x,y in zip(i,q)])
  answer["H(P,Q)"]=buff
  for k, i  in enumerate(np.rot90(matrix),1):
    answer["H(P,B{})".format(k)]=sum([x*y for x,y in zip(i,p)])
for i in [(x,y) for x,y in answer.items()]:
  print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))
# Такой вывод:
# 6 9
# Ответ выйгрыш игрока А в ситуации H(P,Q) = 7.7142
# Ответ выйгрыш игрока А в ситуации H(P,B1) = 10.709999999999999
# Ответ выйгрыш игрока А в ситуации H(P,B2) = 7.739999999999999
# Ответ выйгрыш игрока А в ситуации H(P,B3) = 7.68
# Ответ выйгрыш игрока А в ситуации H(P,B4) = 8.0
# Ответ выйгрыш игрока А в ситуации H(P,B5) = 11.709999999999999
