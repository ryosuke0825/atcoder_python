import math
from decimal import Decimal,  getcontext

A, B = input().split()
a = int(A)
b = Decimal(B)
print(math.floor(a*b))
