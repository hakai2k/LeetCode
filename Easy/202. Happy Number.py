import math
def happy (number):
    n = list(str(number))
    for i in range(len(n)):
        n[i] = int(n[i])
    sum = 0
    for i in n:
        sum += int(math.pow(i, 2))
    return sum

print(happy (19))