n = int(input())

ans = ""
if n < 60:
    h = "00"
    m = "00"
    s = str(n)

elif 60 <= n < 3600:
    h = "00"
    m = str(n//60)
    s = str(n % 60)

else:
    h = str(n//3600)
    m = str((n % 3600)//60)
    s = str((n % 3600) % 60)

if len(h) == 1:
    h = "0"+h
if len(m) == 1:
    m = "0"+m
if len(s) == 1:
    s = "0"+s
print(h + ":" + m + ":" + s)
