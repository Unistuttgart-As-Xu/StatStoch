"""*************************************************************************
  > File Name: Wuefelsumme.py
  > Author: Zhenhao, Xu
  > Mail:tom1049443989@gmail.com
  > Created Time: 2021年11月26日 星期五 03时32分52秒
 ************************************************************************"""

import math


# Wahrscheilichkeit rechnen
class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        t = 1.0/6
        dic = {1: t, 2: t, 3: t, 4: t, 5: t, 6: t}
        x = 1
        while x < n:
            dic1 = {}
            for j in range(1, 7):
                for i in dic.keys():
                    k = j + i
                    if k in dic1.keys():
                        dic1[k] = dic1[k]+dic[i]*t
                        continue
                    dic1.update({k: dic[i] * t})
            dic = dic1
            x += 1
        return dic


# main funktion
s = Solution()
k_s = []
u = 3.5
c_q = 35.0/12
p = 1.0/10
# print("k", "P(W_5=k)")
print("k", "F^{W_5}(k)")
for n in range(2, 41):
    L = {}
    L = s.dicesSum(n)

    # Verteilung ausgeben
    re = []
    for k, p_k in L.items():
        re.append([k, p_k])
#        if n == 5:
#            print(k, p_k, '\n')

    # Verteilungsfunktion ausgeben
    re_f = []
    f = 0.0
    for k, v in L.items():
        f = f + v
        re_f.append([k, f])
        if n == 5:
            print(k, f, '\n')

    # print(re)
    # print('\n')
    # print(re_f)

    # E und E_s ausgeben
#    print('n', 'Epsilon_{neu}', 'Epsilon', '\n')
    for i in range(len(re_f)-1):
        if (re_f[i][1] <= p/2) and (re_f[i+1][1] > p/2):
            k_s.append(re_f[i][0])
            E_s = u - float((re_f[i][0])/n)
            E = math.sqrt(c_q/(n*p))
#            print(n, E_s, E, '\n')
            break
# print(k_s)
