i=2
answer = 0
primeTh = 0
while True:
    prime = True
    for j in range(2, i//2+1):
        if i % j == 0:
            prime = False
            break
    if prime:
        primeTh += 1
    if prime and primeTh == 10001:
        answer = i
        break
    i += 1
print(answer)
