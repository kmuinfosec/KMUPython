import math
N = 50
sieve = [n for n in range(2, N + 1)]
for i in sieve:
    for j in sieve:
        if j > i and j % i == 0:
            sieve.remove(j)

for p in sieve:
    m = 2 ** p - 1
    for j in range(2, int(math.sqrt(m)) + 1):
        if m % j == 0:
            break
    else:
        print(m)
