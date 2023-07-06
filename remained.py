#define prerequisite & ask user for input
num1 = int(input("enter first number: "))
num2 = int(input("enter second number:"))

# the main program (core calculation)
res = num1%num2

# conclusion and output
if res==0:
    print("these 2 numbers are divisible ")
    print("result of devision is: " , (num1/num2))
else:
    print("the left over of dividing" , num1 , "by" , num2 , "is: " , res)