sum = 0
for i in range(2,2000000):
    prime = True
    for j in range(2,i//2+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        sum += i
    if i % 100000 == 0:
        print(i)
print("done")
print(sum)
# TODO: optimize this
# took 2hrs