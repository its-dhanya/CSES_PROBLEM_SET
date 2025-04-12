n = int(input())
arr = list(map(int , input().split()))
dp = [[0 for _ in range(n)]for _ in range(n)]
sumi = sum(arr)
for l in range(n - 1 , -1 , -1):
    for r in range(l , n):
        if l == r:
            dp[l][r] = arr[l]
        else:
            dp[l][r] = max(arr[l] - dp[l + 1][r] , arr[r] - dp[l][r - 1])
print((dp[0][n - 1] + sumi)//2)
