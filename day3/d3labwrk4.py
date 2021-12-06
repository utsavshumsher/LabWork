#Given three integers,print the smallest one.(Three integers should be user input)
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if num1<(num2 and num3):
    print(f"smallest is {num1}")
elif num2<(num1 and num3):
    print(f"smallest is {num2}")
elif num3<(num1 and num2):
    print(f"smallest is {num3}")
else:
    print("all number are equal")