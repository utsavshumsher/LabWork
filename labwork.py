#convert in seconds to day,hours,minutes and seconds
s=int(input("enter the value for seconds:"))
day=(((s/60)/60)/24)
print(f"total day for givevn seconds:{day}")
hour=((s/60)/60)
print(f"total hours for given seconds:{hour}")
minute=(s/60)
print(f"total minutes for given seconds:{minute}")
