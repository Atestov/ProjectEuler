a = 1
b = 2
s = 2

while True:
    for i in range(3):
        a, b = b, a + b
    if b <= 4000000:
        s += b
    else:
        break

print(s)
