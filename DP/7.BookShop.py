n , x = map(int , input().split())
price = list(map(int , input().split()))
pages = list(map(int , input().split()))
dp = [[0 for _ in range(x + 1)] for _ in range(n + 1)]
for i in range(1 , n + 1):
    for j in range(x + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= 0:
            dp[i][j] = max(dp[i][j] , dp[i - 1][j - price[i - 1]] + pages[i - 1])
print(dp[n][x])