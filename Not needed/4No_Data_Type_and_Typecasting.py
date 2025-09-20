A = 1
B = 2.5
Name = "Sanzid"
C = True # True is the correct not true or yse.
D = None # None is the correct not none.

AA = type(A)
BB = type(B)
N = type(Name)
CC = type(C)
DD = type(D)

# print("Data type of A is {AA}") if I want to use this format I need to use f before quotation.

print(f"Data type of A is{AA}")

print("Data type of B is" + str(BB))

# print("Data type of Nmae is {}",format(N)) I use , insteed of . thats whay it is not correct

print("Data type of Nmae is {}".format(N))

print(f"Data type of C is{CC}")

print("Data type of D is"+str(DD))