alphabet = ['c', 'd', 'a', 'b', 'e']
myAlpha = alphabet
print(id(alphabet), id(myAlpha))
alphabet.sort()
print(id(alphabet), id(myAlpha))
