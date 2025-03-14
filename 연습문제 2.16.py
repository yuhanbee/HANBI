import cmath

def rotate_complex(z, degrees):
    """복소수 z를 degrees 만큼 반시계 방향으로 회전"""
    theta = cmath.pi * degrees / 180  
    rotation = cmath.exp(1j * theta)  
    return z * rotation  
z = 1 + 2j

rotated_90 = rotate_complex(z, 90)

rotated_30 = rotate_complex(z, 30)

print(f"회전하기 전 : {z}")
print(f"90도 회전한 후 : {rotated_90}")
print(f"30도 회전한 후 : {rotated_30}")
