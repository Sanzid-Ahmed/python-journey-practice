a = [[1, 2], [3, 4]]

"""
a
│
▼
┌───────────────────────┐
│   ┌────────┐ ┌───────┐│
│   │ [1, 2] │ │[3, 4] ││
│   └────────┘ └───────┘│
└───────────────────────┘

"""

b = a.copy()


"""
a ─────► Outer List A
          │
          ├────► [1, 2]
          │
          └────► [3, 4]


b ─────► Outer List B
          │
          ├────► [1, 2]
          │
          └────► [3, 4]

"""


# See the problem

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)
print(b)




"""
Different outer lists
        +
Same inner lists

"""







a = [[1, 2], [3, 4]]
b = a.copy()

b.append([5, 6])

print(a)
print(b)

