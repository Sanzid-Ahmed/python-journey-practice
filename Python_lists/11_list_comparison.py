a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) 



# Order matters

a = [1, 2, 3]
b = [3, 2, 1]

print(a == b)




a = [1, 2, 3]
b = [1, 2, 4]

print(a != b)




a = [1, 2, 3]
b = [1, 2, 4]

print(a < b)

"""
1 vs 1 → same
2 vs 2 → same
3 vs 4 → 3 is smaller

"""


a = [100, 50]
b = [50, 100]

print(a < b)
