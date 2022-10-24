import math

found = False
for a in range(1, 1000):
    for b in range(1, 1000):
        c = (a*a)+(b*b)
        csqrt = math.sqrt(c)
        if not csqrt.is_integer():
            continue
        if a < b < c:
            if a + b + csqrt == 1000:
                found = True
                break
    if found:
        print("FOUND!")
        print("a={0}, b={1}, c={2}".format(a,b,csqrt))
        print(a*b*csqrt)
        break
