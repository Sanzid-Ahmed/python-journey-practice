a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)







a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)



"""
        ┌───────────────┐
a ─────►│ [1, 2, 3]     │
        │    LIST       │
b ─────►│               │
        └───────────────┘


a ─────► [1, 2, 3]

b ─────► [1, 2, 3]

"""