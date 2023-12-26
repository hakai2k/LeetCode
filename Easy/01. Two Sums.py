def twoSums (num, target):
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] + num[j] == target:
                return [i, j]

num = [10, 20, 30, 40, 10, 20]
target = 70
result = twoSums(num, target)
print(result)