allSet = [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {1, 3, 5, 7, 12, 15},
          {3, 12, 15, 18, 20}, {12, 13, 14, 15, 16, 17, 18, 19}]

for i in range(0, len(allSet) - 1):
    for j in range(i + 1, len(allSet)):
        print(len(allSet[i]&allSet[j]) / len(allSet[i]|allSet[j]))
