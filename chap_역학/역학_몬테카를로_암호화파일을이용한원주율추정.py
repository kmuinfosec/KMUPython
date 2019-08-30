from random import random
from math import sqrt

n = 10000
inside = 0

f = open('normal.txt', 'rb')
#f = open('normal.zip', 'rb')
#f = open('normal.txt.ezc', 'rb')

data = f.read()

for i in range(0, n*2, 2):
    x = data[i]/255
    y = data[i+1]/255
    if sqrt(x*x+y*y) <= 1:
        inside += 1

pi = 4*inside/n

f.close()

print(pi)
