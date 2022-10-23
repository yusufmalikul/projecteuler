# https://projecteuler.net/problem=6
sum = 0
for i in range(1, 101):
    sum += i*i

square = 0
for i in range(1, 101):
    square += i
square = square*square

print(square-sum)
