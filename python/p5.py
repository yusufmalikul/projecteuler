# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
answer = 0
i = 0
while True:
    i += 1
    divisible = False
    for j in range(1,21):
        if i % j == 0:
            divisible = True
        else:
            divisible = False
            break
    if divisible:
        answer = i
        break
print(answer)
# 2m 4s
