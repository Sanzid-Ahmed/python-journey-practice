"""
append()
extend()
insert()

"""



# append.
# Basic append 
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# append anythings
numbers.append("Sanzid")
numbers.append([50, 60])
print(numbers)

"""
1. adds one element at the end of the list.
2. whole list as one element.

"""





# extend
# Basic extend 
numbers = [10, 20, 30]
print(numbers)


numbers.extend([40, 50, 60])
print(numbers)

"""
1. adds the elements of another iterable individually.

append  → add ONE thing
extend  → add MANY things

"""





# insert
# Basic insert
numbers = [10, 20, 30]
print(numbers)


numbers.insert(99, 1)
print(numbers)

numbers.insert(1, 99)
print(numbers)

