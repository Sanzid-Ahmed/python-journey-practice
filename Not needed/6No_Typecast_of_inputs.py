#int <-> float
a = input("Enter float number:\n") #taking input as string
print(a)

b = int(float(a)) #convert the string into float then int.

print(b)
#-----------------------------------------------------------------------------------------------------------------------------------------





# Character <-> ASCII
c = input("Enter an alphabet:\n")
print(c)

print(ord(c))


# d = input("Enter an ASCII value:\n")



# It is not correct because in Python, input() always returns a string, no matter what the user types.
# So I need to convert the input into requared format from string.



# there are two way to convert correct user given formet from string
# 1No directly at the time of taking input. variable = data_type(input("Enter a value:\n"))
# or separately by declaring a separate variable.

d = int(input("Enter an ASCII value:\n"))

print(chr(d))
#-------------------------------------------------------------------------------------------------------------------------------------------




# boolean =>
# e = input("Are you a stuent?\n").lower == 'yes'

e = input("Are you a stuent?\n").lower() == 'yes' #need to yse () after .lower

print(e)