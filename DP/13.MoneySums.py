n = int(input())
arr = list(map(int , input().split()))
sumarr = sum(arr)
dp = [[False for _ in range(sumarr+ 1)] for _ in range(n + 1)]
dp[0][0] = True
for i in range(1 , n + 1):
    for sumi in range(sumarr + 1):
        dp[i][sumi] = dp[i - 1][sumi]
        if sumi >= arr[i - 1] and dp[i - 1][sumi - arr[i - 1]]:
            dp[i][sumi] = True
ans = []
for i in range(1 , sumarr + 1):
    if dp[n][i]:
        ans.append(i)
print(len(ans))
print(' '.join(map(str , ans)))
