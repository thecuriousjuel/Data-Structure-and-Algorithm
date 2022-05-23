def f_knapsack(n, w, profit, weight):
    p_by_w = [profit[i] / weight[i] for i in range(n)]

    taken = [0] * n

    for i in range(n):
        max_select = 0
        for j in range(n):
            if taken[j] != 0:
                continue

            if p_by_w[j] > max_select:
                max_select = p_by_w[j] 
                max_select_index = j

    
        if w - weight[max_select_index] < 0:
            taken[max_select_index] = w / weight[max_select_index] 
            break
        else:
            w -= weight[max_select_index]
            taken[max_select_index] = 1


    for i in range(n):
        if taken[i] != 0:
            print('Item {} is taken. Amount taken = {:.2f}'.format(i, taken[i]))

    s = 0
    for i in range(n):
        s += taken[i] * profit[i]

    print('The total cost is : {:.2f}'.format(s))


n = 4
w = 50
profit = [60, 40, 100, 120]
weight = [10, 40, 20, 30]

f_knapsack(n, w, profit, weight)

# ---------------------------------------------------------------------

# n = 7
# w = 15

# profit = [10, 5, 15, 7, 6, 18, 3]
# weight = [2, 3, 5, 7, 1, 4, 1]

# f_knapsack(n, w, profit, weight)