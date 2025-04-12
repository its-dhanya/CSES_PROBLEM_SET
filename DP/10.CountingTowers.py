dp =[[0 for _ in range(2)]for _ in range(10 ** 6 + 1)]
dp[1][0] = dp[1][1] = 1
mod = int(1e9 + 7)
for i in range(2 , 10 ** 6 + 1):
    dp[i][0] = (2 * dp[i - 1][0] + dp[i - 1][1]) % mod
    dp[i][1] = (4 * dp[i - 1][1] + dp[i - 1][0]) % mod
t = int(input())
while t:
    n = int(input())
    print((dp[n][0] + dp[n][1])% mod)
    t -= 1