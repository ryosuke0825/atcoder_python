s = input()
odd = s[0::2]
even = s[1::2]

odd0 = odd.count("0")
odd1 = odd.count("1")
even0 = even.count("0")
even1 = even.count("1")

print(min((odd0 + even1), (odd1 + even0)))
