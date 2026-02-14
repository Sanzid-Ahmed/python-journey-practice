Input = input("Enter the input: ")
answer = Input.split()
int_answer = map(int, answer)
# map return object and we can not see the object acurate value so we need to convert it into list. 
list_answer = list(int_answer)
print(list_answer)