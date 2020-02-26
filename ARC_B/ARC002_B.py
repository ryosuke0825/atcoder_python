import datetime
y, m, d = input().split('/')
day = datetime.date(int(y), int(m), int(d))

while True:
    y = day.year
    m = day.month
    d = day.day

    if y/m % d == 0:
        break

    day += datetime.timedelta(days=1)

print(str(y)+'/'+str(m).zfill(2)+'/'+str(d).zfill(2))
