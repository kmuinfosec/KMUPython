dic = {2015123: "Alice", 2015200: "Bob", "KMU": "JeongReung"}

del dic[2015123]
print(dic)

x = dic.pop("KMU")
print(dic)
print(x)
