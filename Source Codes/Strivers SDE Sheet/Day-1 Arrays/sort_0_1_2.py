nums = [2, 0, 1, 0, 2, 1, 1, 2, 0]

count_0 = 0
count_1 = 0
count_2 = 0


for i in nums:
    if i == 0:
        count_0 += 1

    if i == 1:
        count_1 += 1

    if i == 2:
        count_2 += 1


l = [0 for _ in range(count_0)] + [1 for _ in range(count_1)] + [2 for _ in range(count_2)]
print(l)
