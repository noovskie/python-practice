leap_year = int(input())

if leap_year % 4 == 0 and (not leap_year % 100 == 0):
    print('leap year')
elif (leap_year % 100 == 0) and (leap_year % 400) == 0:
    print('leap year')
else:
    print('not a leap year')