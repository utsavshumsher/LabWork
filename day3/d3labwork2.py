e=int(input("Enter marks obtained in English:"))
n=int(input("Enter marks obtained in Nepali:"))
c=int(input("Enter marks obtained in Computer:"))
m=int(input("Enter marks obtained in Math:"))
T=e+n+c+m
print(f"Total marks obtained is {T}.")
P=(T/400)*100
print(f"Percentage obtained by student is {P} %.")

if P>70:
    print("Distinction")
elif P>60:
    print("First Division")
elif P>40:
    print("Pass")
elif P<40:
    print("Fail")
    