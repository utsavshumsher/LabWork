# Take username and password from user and check it again for the three times whether the user has entered the right
# username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
# for consecutive 3 times and if the limit exceeds than print "Attempt finished".

user = input("Enter your username")
password = input("Enter your password")

for i in range(0, 3):
    username1 = input("Enter username")
    password1 = input("Enter password")
    if user == username1 and password == password1:
        print("You are logged in successfully")
        break
    # else:
    #     print("invalid credentials")
    elif i<3:
        if user != username1 and password != password1 and i<3:
            print("Invalid Credentials Try again")
else:
    print("Attempt finished")