n , m = map(int, input().split())
arr = list(map(int , input().split()))
dp = [[0 for _ in range(m + 2)] for _ in range(n + 1)]
mod = 10 ** 9 + 7
for i in range(n):
    if i == 0:
        if arr[0] == 0:
            for val in range(1 , m + 1):
                dp[i][val] = 1
        else:
            dp[i][arr[0]] = 1
    else:
        if arr[i] == 0:
            for val in range(1 , m + 1):
                dp[i][val] = (dp[i][val] +dp[i - 1][val - 1] + dp[i - 1][val] + dp[i - 1][val + 1]) % mod
        else:
            dp[i][arr[i]] = (dp[i - 1][arr[i] - 1] + dp[i - 1][arr[i]] + dp[i - 1][arr[i] + 1]) % mod
ans = 0
for i in range(1 , m + 1):
    ans = (ans + dp[n - 1][i]) % mod
print(ans)
            
