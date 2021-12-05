#convert minute into hours and minutes
N=int(input("Enter the number of minutes that is passed since midnight"))
hours = N // 60
minutes = N % 60
time="{}:{}".format(hours,minutes)
print(time)
