"""*************************************************************************
  > File Name: G_dis_Verteilung.py
  > Author: Zhenhao, Xu
  > Mail:tom1049443989@gmail.com
  > Created Time: 2021年12月09日 星期四 21时37分36秒
 ************************************************************************"""


import math
import numpy as np


list_Omega = []
dic_pw = {}
dic_P = {}
list_x = []
list_y = []


# for i in range(1, 7):
#    for j in range(1, 7):
#        list_Omege.append((i, j))

for i in range(1, 6):
    for j in range(1, 6):
        if i == j:
            continue
        for m in range(1, 6):
            if (m == j) or (m == i):
                continue
            for n in range(1, 6):
                if (n == m) or (n == j) or (n == i):
                    continue
                for k in range(1, 6):
                    if (k == m) or (k == j) or (k == i) or (k == n):
                        continue
                    print((i, j, m, n, k))
                    list_Omega.append((i, j, m, n, k))


def Funktion_X(w1):
    return w1[0]


def Funktion_Y(w2):
    count = 0
    for i in range(0, 5):
        if w2[i] == (i+1):
            count = count + 1
    return count


for i in list_Omega:
    dic_pw.update({i: 1.0/len(list_Omega)})
    xx = Funktion_X(i)
    yy = Funktion_Y(i)
    xy = (xx, yy)
    if xy in dic_P.keys():
        dic_P[xy] = dic_P[xy] + dic_pw[i]
    else:
        dic_P.update({xy: dic_pw[i]})

    if (xx in list_x) is False:
        list_x.append(xx)

    if (yy in list_y) is False:
        list_y.append(yy)
r_max = len(list_x)
s_max = len(list_y)
print(" X(Omega)=", list_x, '\n', "Y(Omega)=", list_y)

E_x = 0
E_y = 0
E_xy = 0
for xy2 in dic_P.keys():
    E_x = E_x + xy2[0] * dic_P[xy2]
    E_y = E_y + xy2[1] * dic_P[xy2]
    E_xy = E_xy + xy2[0] * xy2[1] * dic_P[xy2]
    print("P(X, Y)=", "P", xy2, "=", dic_P[xy2])
C_xy = E_xy - E_x * E_y
print("E(X)=", E_x, "E(Y)=", E_y, "E(XY)=", E_xy, "C(X,Y)=", C_xy)
"""
 X(Omega)= [1, 2, 3, 4, 5]
 Y(Omega)= [5, 3, 2, 1, 0]
P(X, Y)= P (1, 5) = 0.008333333333333333
P(X, Y)= P (1, 3) = 0.049999999999999996
P(X, Y)= P (1, 2) = 0.06666666666666667
P(X, Y)= P (1, 1) = 0.075
P(X, Y)= P (2, 3) = 0.008333333333333333
P(X, Y)= P (2, 1) = 0.075
P(X, Y)= P (2, 0) = 0.09166666666666666
P(X, Y)= P (2, 2) = 0.025
P(X, Y)= P (3, 2) = 0.025
P(X, Y)= P (3, 0) = 0.09166666666666666
P(X, Y)= P (3, 1) = 0.075
P(X, Y)= P (3, 3) = 0.008333333333333333
P(X, Y)= P (4, 1) = 0.075
P(X, Y)= P (4, 0) = 0.09166666666666666
P(X, Y)= P (4, 2) = 0.025
P(X, Y)= P (4, 3) = 0.008333333333333333
P(X, Y)= P (5, 0) = 0.09166666666666666
P(X, Y)= P (5, 1) = 0.075
P(X, Y)= P (5, 2) = 0.025
P(X, Y)= P (5, 3) = 0.008333333333333333
E(X)= 3.0 E(Y)= 1.0 E(XY)= 2.5 C(X,Y)= -0.5
"""
