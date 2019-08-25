# 유클리드 알고리즘 개선
print("Type big number first, then small one")
a = int(input("a="))
b = int(input("b="))

while b:
    a, b = b, a % b
print("GCD is %d" %a)
