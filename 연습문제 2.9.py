print("섭씨   화씨")
for celsius in range(0, 51, 10):
    fahrenheit = (9 / 5) * celsius + 32
    print(f"{celsius:<5} {fahrenheit:.1f}")
