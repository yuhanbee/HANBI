import math
def volume_cube(s):
    return s**3
def volume_rectangular_prism(l, w, h):
    return l * w * h
def volume_cone(r, h):
    return (1/3) * math.pi * r**2 * h
def volume_sphere(r):
    return (4/3) * math.pi * r**3

def volume_cylinder(r, h):
    return math.pi * r**2 * h

# 1) 
s1 = 12
print(f"모서리의 길이가 12인 정육면체의 부피: {volume_cube(s1)}")
# 2) 
s2 = 20
print(f"모서리의 길이가 20인 정육면체의 부피: {volume_cube(s2)}")
# 3)
l, w, h = 3, 5, 6
print(f"가로, 세로, 깊이가 각각 3, 5, 6인 직육면체의 부피: {volume_rectangular_prism(l, w, h)}")
# 4)
r, h_cone = 20, 10
print(f"반지름과 높이가 각각 20, 10인 원뿔의 부피: {volume_cone(r, h_cone)}")
# 5)
r_sphere = 15
print(f"반지름이 15인 구의 부피: {volume_sphere(r_sphere)}")
# 6)
r_cylinder, h_cylinder = 20, 10
print(f"반지름과 높이가 각각 20, 10인 원기둥의 부피: {volume_cylinder(r_cylinder, h_cylinder)}")
