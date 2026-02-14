# NO: 01 if
if 5 > 2:
    print("Five is greater then two!")


# NO: 02 if-else
x = 2

if x > 0: 
    print("Positive")
else: 
    print("Not Positive")



# NO: 03 if-elif-else
x = 5

if x > 0: 
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")



# NO: 04 Nested
x = 5
y = 3

if x > 0: 
    if x > y: 
        print("Hello!")
    else:
        print("Bye!")
else: 
    print("Negative.")


# NO: 05 match-case
day = 1

match day:
    case 1: 
        print("Saturday")
    case 2: 
        print("Sunday")
    case 3: 
        print("Monday")
    case _:
        print("Invalid")



# Summery
# 1. if
# 2. if-else
# 3. if-elif-else
# 4. Nested
# 5. match-case