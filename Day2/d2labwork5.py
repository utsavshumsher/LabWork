G1=int(input("enter the number of student in first class"))
G2=int(input("enter the number of student in second class"))
G3=int(input("enter the number of student in third class"))

D1=(G1//2)
print(f"the required number of desk for first class is {D1}")

D2=(G2//2)
print(f"the required number of desk for second class id {D2}")

D3=(G3//2)
print(f"the required number of desk for third class {D3}")

R1=(G1%2)
print(f"remaining desk for first class is {R1}")

R2=(G2%2)
print(f"remaining desk for second class is {R2}")

R3=(G3%2)
print(f"remaining desk for third class is {R3}")

T=D1+D2+D3+R1+R2+R3
print(f"total number of desks that can be purchased is {T}")