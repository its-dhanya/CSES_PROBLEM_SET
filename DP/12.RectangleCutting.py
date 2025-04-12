a , b = map(int , input().split())
dp = [[float('inf') for _ in range(b + 1)] for _ in range(a + 1)]
for i in range(1 ,  a + 1):
    for j in range(1 , b + 1):
        if i == j:
            dp[i][j] = 0
            continue
        for k in range(1 , i):
            dp[i][j] = min(dp[i][j] , dp[k][j] + dp[i - k][j] + 1)
        for l in range(1 , j):
            dp[i][j] = min(dp[i][j] , dp[i][l] + 1 + dp[i][j - l])
print(dp[a][b])
