import math

multiples = []
sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples.append(i)
        sum += i


print(sum)
