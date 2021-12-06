#Given a n-digit number. Find the sum of its digits.
number=int(input("enter a number"))
total=0
while number>0:
    digits=number%10
    total=total+digits
    number=number//10
print("The sum of digits of the number entered is", total)