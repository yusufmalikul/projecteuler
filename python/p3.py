# TODO: Optimize this
# I found the answer but the program still running
t = 600851475143
answer = 0
limit = t//2
for i in range(2, limit):
    if t % i == 0:
        # print(i)
        # check if prime
        prime = True
        for k in range(2, i):
            if i % k == 0:
                prime = False
                break
        if prime:
            answer = i
print(answer)
