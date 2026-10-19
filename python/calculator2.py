def Exponents(num1 , num2):
    return num1 ** num2

def Multiplication(num1 , num2):
    return num1 * num2

def Division(num1 , num2):
    return num1 / num2

def Addition(num1 , num2):
    return num1 + num2

def Subtraction(num1 , num2):
    return num1 - num2
num1 = int(input("Enter the frist number: ")) 
calculation = input("Chose The calculation: (^ , * , / , - , +): ")
num2 = int(input("Enter the second number: "))
if calculation == "^":
    print(Exponents(num1 , num2)) 
elif calculation == "*":
    print(Multiplication(num1 , num2))
elif calculation == "/":
    print(Division(num1 , num2))
elif calculation == "+":
    print(Addition(num1 , num2))
elif calculation == "-":
    print(Subtraction(num1 , num2))
else:
    print("sorry, You chose an incorrect calculation.")