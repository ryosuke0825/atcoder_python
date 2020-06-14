import math

oa, ab, bc = map(int, input().split())

area = (oa+ab+bc)*(oa+ab+bc)*math.pi
side_list = [oa, ab, bc]
side_list.sort()
if not(side_list[0]+side_list[1] >= side_list[2]):
    side = min(abs(oa+ab-bc), abs(ab+bc-oa), abs(ab-bc-oa))
    area -= side*side*math.pi
print(area)
