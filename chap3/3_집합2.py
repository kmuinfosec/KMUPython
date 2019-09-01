prime_numbers = {2, 3, 5, 7}

print("추가 전 :", prime_numbers)
# 원소 한 개를 추가할 때는 add를 사용한다.
prime_numbers.add(11)
print("11 추가 후 :", prime_numbers)
# 여러 개의 원소를 추가할 때는 update를 사용한다.
prime_numbers.update([13, 17, 19])
print("[13, 17, 19] 추가 후 :", prime_numbers)
