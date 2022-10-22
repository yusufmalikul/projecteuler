sum = 0
a = 1
b = 2
i = 3
print(b)
while True:
    if b % 2 == 0:
        sum += b
    # without temp variable we can use:
    # a, b = b, a + b
    temp_a = a
    a = b
    b = temp_a + b
    i += 1
    if b >= 4000000:
        break
print(sum)
