c = input()
al = ["Sunny", "Cloudy", "Rainy"]

if al.index(c) < 2:
    print(al[al.index(c)+1])
else:
    print("Sunny")
