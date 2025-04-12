n , x = map(int , input().split())
coins = list(map(int , input().split()))
dp = [float('inf')] * (x + 1)
dp[0] = 0
for sumi in range(1 , x + 1):
    for c in range(n):
        if coins[c] <= sumi:
            dp[sumi] = min(dp[sumi] , dp[sumi - coins[c]] + 1)
print(dp[x] if dp[x] != float('inf') else -1)
