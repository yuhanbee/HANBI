src = 'a2b3c6a2c3f1g1'
output = ''
i = 0
while i < len(src):
    ch = src[i] 
    num = int(src[i + 1])
    output += ch * num
    i += 2 
print("src =", src)
print("output =", output)
