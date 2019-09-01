a = [8, 4, 9, 5]
small = a[0]
for i in range(1, len(a)):
    if small > a[i]:
        small = a[i]
print(small)
