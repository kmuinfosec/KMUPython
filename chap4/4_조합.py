def combi(n,r):
    res1 = 1
    res2 = 1
    if n>1:
        for i in range(r):
            res1 *= n
            res2 *= r
            n, r = n-1, r-1
        return res1//res2
    else:
        return "자연수를 입력해주세요."

print(combi(5,2))
