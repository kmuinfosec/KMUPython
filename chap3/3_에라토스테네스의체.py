eratosthenes = []

for i in range(2,65):
    eratosthenes.append(i)
print(eratosthenes)
for i in eratosthenes:
    for j in eratosthenes:
        if j>i and j%i==0:
            eratosthenes.remove(j)
print(eratosthenes)
