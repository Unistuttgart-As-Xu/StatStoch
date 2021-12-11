"""*************************************************************************
  > File Name: Sammelbilder.py
  > Author: Zhenhao, Xu
  > Mail:tom1049443989@gmail.com
  > Created Time: 2021年10月30日 星期六 17时02分10秒
 ************************************************************************"""
import random

numOfPictures = 10   # n
iterations = 2 ** 5

totalSchokoriegel = 0
schokoriegelToNext = [0 for i in range(0, numOfPictures)]

for i in range(iterations):
    collection = [False for i in range (numOfPictures)]
    isFull = False
    currentPictures = 0
    schokoriegelNeeded = 0

    while (isFull == False):
        schokoriegelNeeded += 1
        totalSchokoriegel += 1
        randint = random.randint(0, numOfPictures-1)

        if (collection[randint] == False):
            collection[randint] = True
            schokoriegelToNext[currentPictures] += schokoriegelNeeded
            schokoriegelNeeded = 0
            currentPictures += 1

        isFull = True
        for j in range(len(collection)):
            if (collection[j] == False):
                isFull = False


for i in range(len(schokoriegelToNext)):
    schokoriegelToNext[i] = round(schokoriegelToNext[i] / iterations, 2)
print(schokoriegelToNext)
print(f'Durschschnittliche Schokoriegel: {round(totalSchokoriegel / iterations, 2)}')

# a)
# durschnittliche Schokoriegel fÃ¼r n = 63:  1. 296,02
#                                           2. 296,68
#
#  b)
#   1. Durchlauf    2. Durchlauf
#   0               0
#   1.0             1.0
#   1.11            1.11
#   1.25            1.25
#   1.42            1.42
#   1.67            1.67
#   2.00            2.02
#   2.50            2.49
#   3.32            3.36
#   4.98            5.0
#   10.03           10.05
#   Durschschnittliche Schokoriegel: 29.29 / 29.38
#
