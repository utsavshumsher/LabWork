#to print total number of benches needed
import math
a=int(input("Enter total number of students in a class:"))
b=float(input("Enter total number of students in b class:"))
c=float(input("Enter total number of students in c class:"))
print(math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2))
    
    