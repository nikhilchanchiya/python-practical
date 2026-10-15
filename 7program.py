def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

print("------manu------")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("please select the choice (1-4):"))
num1 = int(input("please enter num1:"))
num2 = int(input("please enter num2:"))

if choice==1:
    print("Addition =",addition(num1,num2))
elif choice==2:
    print("Subtraction =",subtraction(num1,num2))
elif choice==3:
    print("Multiplication =",multiplication(num1,num2))
elif choice==4:
    if(num2 != 0):
        print("Division =",division(num2,num1))
    else:
     print("can not divide by zero")
else:
    print("invalid choice")