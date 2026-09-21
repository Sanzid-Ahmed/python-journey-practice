"""
a = [[10, 20], [30, 40]] 
b = a.copy() 

b[0].append(50) 

print(a) 
print(b) 


ans: 
[[10, 20, 50], [30, 40]] 
[[10, 20, 50], [30, 40]]








a = [[10, 20], [30, 40]] 
b = a.copy() 

b.append([50, 60]) 

print(a) 
print(b)

ans: 
[[10, 20], [30, 40]] 
[[10, 20], [30, 40], [50, 60]] 

"""



# Varify 

a = [[10, 20], [30, 40]] 
b = a.copy() 

b[0].append(50) 

print(a) 
print(b) 


a = [[10, 20], [30, 40]] 
b = a.copy() 

b.append([50, 60]) 

print(a) 
print(b)