from copy import deepcopy
a = [1,2,3,[4,5,6]]
b = a.copy()
c = deepcopy(a)
a[0] = 100
a[3][0] = 20
print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')
print(a is c)
print(a is b)