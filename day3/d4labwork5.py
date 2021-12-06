h=int(input("Number of classes held"))
a=int(input("Number of class attended"))
p=a/h*100
print(f"Percentage of class attended is {p}%.")
if p>=75:
    print("Student is allowed to sit in exam .")
else:
    print("Student is not allowed to sit in exam")
 