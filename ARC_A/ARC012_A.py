day_of_week = ['Saturday', 'Friday', 'Thursday',
               'Wednesday', 'Tuesday', 'Monday', 'Sunday']
day = input()
if day == 'Sunday':
    day = 'Saturday'
print(day_of_week.index(day))
