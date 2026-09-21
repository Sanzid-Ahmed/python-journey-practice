"""
remove()
pop()
clear()

"""



# remove
# Basic remove
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)


# value doesn't exist
# numbers.remove(50)
# print(numbers)



# value appears multiple times
numbers = [10, 20, 20, 30]
numbers.remove(20)
print(numbers)



"""
1. Find the value 30 and remove it. 
2. Uses the value, NOT the index. 
3. value doesn't exist. => ValueError
4. value appears multiple times. => removes the first matching value only. 
"""







# pop
# Basic pop
numbers = [10, 20, 30, 40]
x = numbers.pop(2)
print(numbers)
print(x)



# pop without index
numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)


"""
1. Removes an element by index. 
2. Returns the removed element.
3. pop without index pop(), removes the last element. 
"""











# clesr
# Basic clear
numbers = [10, 20, 30, 40]
numbers.clear()
print(numbers)


"""
removes everything from the list.

"""
