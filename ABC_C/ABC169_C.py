import math
from decimal import Decimal,  getcontext

getcontext().prec = 100
A, B = input().split()
a = int(A)
b = Decimal(B)
print(math.floor(a*b))
