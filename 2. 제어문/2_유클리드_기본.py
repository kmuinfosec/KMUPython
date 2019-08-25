# 유클리드 알고리즘 기본
print("Type big number first, then small one")
a = int(input("a="))
b = int(input("b="))

while b != 0:
    x = a
    a = b
    b = x % b
print("GCD is %d" %a)
