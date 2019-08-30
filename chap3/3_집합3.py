prime_numbers = {2, 3, 5, 7, 9, 11, 13, 15, 17, 19}

print("원소 삭제 전 :", prime_numbers)
prime_numbers.discard(9)
print("9 삭제 후 :", prime_numbers)
prime_numbers.remove(15)
print("15 삭제 후 :", prime_numbers)
