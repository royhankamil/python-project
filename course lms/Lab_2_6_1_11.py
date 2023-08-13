hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
new_mins = (mins + dura) % 60
new_hour = (hour + (mins + dura) // 60) % 24

print(new_hour, new_mins, sep=":")
