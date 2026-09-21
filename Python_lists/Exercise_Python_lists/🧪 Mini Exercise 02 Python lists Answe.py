"""
numbers = [10,  20,  30]


1. numbers.append(40)
ans: [10, 20, 30, 40]

2. numbers.extend([50, 60]) 
ans: [10, 20, 30, 40, 50, 60]

3. numbers.insert(1, 99) 
ans: [10, 99, 20, 30, 40, 50, 60]

"""



# verify answer: 

numbers = [10,  20,  30]

numbers.append(40)
print(numbers)

numbers.extend([50, 60])
print(numbers)
 
numbers.insert(1, 99)
print(numbers)


# code test 01

items = ["A","B", "C"]
items.append(["D", "E"])

""" 
ans: ["A","B", "C", ["D", "E"]]

"""

print(items)
