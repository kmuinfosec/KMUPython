c = "내가 그린 그림은 긴 기린 그린 그림이고 네가 그린 기린 그림은 안 긴 기린 그림이다."
pa = "그림"
gr = "기린"
result = (
    "내가 그린 %s은 긴 %s 그린 %s이고 네가 그린 %s %s은 안 긴 %s %s이다."
    % (pa, gr, pa, gr, pa, gr, pa))
print(c)
print(result)
