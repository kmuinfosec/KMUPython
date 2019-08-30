dic = {2015123: "Alice", 2015200: "Bob", "KMU": "JeongReung"}
dic[2015300] = "Carole"
dic.update({2015400: "Dave", 2015500: "Eve"})
print(dic)
print(dic["KMU"])
print(dic[2015200])
print(dic["Alice"])
