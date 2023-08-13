year = int(input("Enter a year: "))

#
# Write your code here.
#	

if year < 1582:
    print("Not within the Gregorian calender period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("leap year")
else:
    print("leap year")
