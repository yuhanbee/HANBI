def inch_cm(inch):
    cm = inch * 2.54
    return cm
for inch in range(1,6):
    print(f"{inch}인치 = {inch_cm(inch):.2f} 센티미터")
