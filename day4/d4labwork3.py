age=int(input("Enter age"))
print ("Gender? (M or F)")
gender = input()
if (gender =="F" or gender =="f") and 20 <= age <= 60:
  print ("Urban areás only")
elif (gender == "M" or gender == "m") and 20 <= age <= 40:
    print ("You can work anywhere")
elif (gender == "M" or gender=="m") and 40 < age <= 60:
   print("Urban areas only")
else:
    print("error")