"""
numbers = [10, 20, 30, 40, 50]

1. numbers.remove(30)
ans: [10, 20, 40, 50]


2. x = numbers.pop(1)
   print(numbers)
   print(x)

ans: [10, 40, 50]
     x = 20

     
3. numbers.pop()
ans: [10, 40]


4. numbers.clear()
ans: []

"""


# Varify answer

numbers = [10, 20, 30, 40, 50] 

numbers.remove(30) 
print(numbers) 


x = numbers.pop(1) 
print(numbers) 
print(x) 


numbers.pop() 
print(numbers) 


numbers.clear()
print(numbers)