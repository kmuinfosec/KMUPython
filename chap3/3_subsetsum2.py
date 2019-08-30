from itertools import combinations
A = {-7, -3, -2, 5, 8}
ans = False
for i in range(1, len(A) + 1):
    pos = list(combinations(A, i))
    for j in pos:
        if sum(j) == 0:
            ans = True
            print(j) # 0이되는 부분집합 출력
            break
    if ans:
        break

if ans:
    print('true')
else:
    print('false')
