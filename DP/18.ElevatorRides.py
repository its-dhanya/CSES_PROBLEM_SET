n , x = map(int , input().split())
weights = list(map(int , input().split()))
dp = [(n + 1 , 0)] * (1 << n)
dp[0] = (1 , 0)
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            continue
        newmask = mask | (1 << i)
        ride , curweigh = dp[mask]
        if curweigh + weights[i] <= x:
            dp[newmask] = min(dp[newmask] , (ride , curweigh + weights[i]))
        else:
            dp[newmask] = min(dp[newmask] , (ride + 1 , weights[i]))
print(dp[(1 << n) - 1][0])