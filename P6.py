import datetime
c_y = datetime.date.today().year
f_y = int(input("Enter the final year : "))
if f_y < c_y:
    print("Final year must be greater than or equal to the current year")
else:
    print(f"Leap years from {c_y} to {f_y}")
    for year in range(c_y, f_y+1):
        if(year % 4==0 and year%100!=0)or(year%400==0):
             print(year)
