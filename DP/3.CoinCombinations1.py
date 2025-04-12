n , x = map(int , input().split())
coins = list(map(int , input().split()))
dp = [0] * (x + 1)
dp[0] = 1
mod = 10 ** 9 + 7
for sumi in range(1 , x + 1):
    for c in range(n):
        if coins[c] <= sumi:
            dp[sumi] = (dp[sumi] + dp[sumi - coins[c]]) % mod
print(dp[x] % mod)
