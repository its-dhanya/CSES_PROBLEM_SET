n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
grid = []
mod = 10** 9 + 7
for i in range(n):
    grid.append(list(input().strip()))
if grid[0][0] == '*' or grid[n - 1][n - 1] == '*':
    print(0)
    exit()
dp[0][0] = 1
for i in range(1, n):
    if grid[0][i] == '*':
        break
    dp[0][i] = dp[0][i - 1] % mod
for i in range(1, n):
    if grid[i][0] == '*':
        break
    dp[i][0] = dp[i - 1][0] % mod
for i in range(1, n):
    for j in range(1, n):
        if grid[i][j] == '*':
            dp[i][j] = 0
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod
print(dp[n - 1][n - 1] % mod)