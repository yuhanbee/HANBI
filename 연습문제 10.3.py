#연습문제 10.3
s= 'Hello World~'
methods = ['pop','sort', 'append','upper', 'insert', 'remove']

print(" 사용 가능한 메서드:")
for method in methods:
    if hasattr(s, method):
        print(f"- {method}()")

print("\n 사용 불가능한 메서드:")
for method in methods:
    if not hasattr(s, method) :
        print(f"- {method}()")
