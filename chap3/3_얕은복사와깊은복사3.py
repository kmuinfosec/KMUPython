import copy

alphabet = ['c', 'd', 'a', 'b', 'e']
alpha_copy = copy.deepcopy(alphabet)
print(id(alphabet), id(alpha_copy))
alpha_copy.sort()
print(id(alphabet), id(alpha_copy))
