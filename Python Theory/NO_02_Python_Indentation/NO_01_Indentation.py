number1 = 33
number2 = 255

if number1 > number2:
    print("number1 is greater than number2")
# this code will give nothing because if block runs only when the condition is True. 
else:
    print("number2 is greater then number1")

# Here if we want to print the direct value of the number1 and number2 then there are sevarale ways: 
"""
1. Comma-separated (Like = JavaScript)
    print("number1 = ", number1, "and number2 = ", number2)

2. String concatenation (Like = Java)
    print("number1 = " + str(number1) + ", number2 = " + str(number2))

3. %-formatting (Like = C)
    print("number1 = %d, number2 = %d" % (number1, number2))

4. f-string [**best choice]
    print(f"number1 = {number1}, number2 = {number2})
    
5. format() method
    print("number1 = {}, number2 = {}".format(number1, number2))
"""


if number1 > number2: 
    print(f"{number1} is greater then {number2}")
else:
    print(f"{number2} is greater then {number1}")