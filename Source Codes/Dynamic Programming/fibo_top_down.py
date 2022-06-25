# Code 1 : Working code

# n = 8

# dp = {0:0, 1:1}

# for i in range(2, n+1):
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[n])


# Code 2 :

n = 7
count = 0

a = 0
b = 1
c = 0


while count < n:
    c = a + b
    b = a
    a = c

    count += 1
    
print(c)



