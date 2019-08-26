import hashlib

s = '''\
Index: 4
Timestamp: Thu Jul 25 16:20:00 2019
Difficulty: 3
Nonce: {Nonce}
PrevHash: e4d7f1b4ed2e42d15898f4b27b019da4\
'''

dfficulty = 3
nonce = 0
while True:
    result = hashlib.md5(bytes(s.format(Nonce=nonce), encoding='utf8'))
    hash = result.hexdigest()
    for j in range(0, dfficulty):
        if hash[j] != '0':
            break
    else:
        print(hash)
        break
    nonce += 1
print(nonce)
