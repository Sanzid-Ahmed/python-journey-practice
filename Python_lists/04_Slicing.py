# Syntax => list[start: stop]
# start = is included. 
# stop = is excluded. 


numbers = [10, 20, 30, 40, 50]


# Basic test: 
print(numbers[1:4])


print(numbers[:3])


print(numbers[2:])


print(numbers[:])




# step
print(numbers[0:5:2])

"""
Meaning: 

start = 0
stop = 5
step = 2
"""


# reverse a list
print(numbers[::-1])

"""
numbers[start:stop:step]
numbers[::-1]


start = empty → use the end
stop  = empty → go to the beginning
step  = -1    → move backwards


numbers[::1]    # forward
numbers[::-1]   # backward

"""