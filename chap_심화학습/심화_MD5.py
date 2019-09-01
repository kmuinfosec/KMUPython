import hashlib

message = 'hello, SangGeon' # 해시화할 문자열
message_bytes = bytes(message, encoding='utf8') # bytes로 변환하기
print(message) # 문자열 출력
print(message_bytes) # bytes로 변환된 문자열 출력
result = hashlib.md5(message_bytes)
print(result.digest()) # md5 해시화된 결과 bytes 출력
print(result.hexdigest()) # md5 해시화된 결과 bytes를 16진수로 출력
