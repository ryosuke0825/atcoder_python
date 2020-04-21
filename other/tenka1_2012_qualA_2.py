import re

S = input()
print(re.sub(r' +', ',', S))
