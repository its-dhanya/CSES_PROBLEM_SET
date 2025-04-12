n , x = map(int , input().split())
coins = list(map(int , input().split()))
dp = [0] * (x + 1)
dp[0] = 1
mod = 10 ** 9 + 7
for c in coins:
    for sumi in range(1 , x + 1):
        if c <= sumi:
            dp[sumi] = (dp[sumi] + dp[sumi - c]) % mod
print(dp[x] % mod)

