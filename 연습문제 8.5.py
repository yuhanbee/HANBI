import math
for angle in range(0, 181, 10):
    radian = math.radians(angle)
    print(f"sin({angle}) = {math.sin(radian):.3f}, cos({angle}) = {math.cos(radian):.3f}, tan({angle}) = {math.tan(radian):.3f}")
