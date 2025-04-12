n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
mod = 10 ** 9 + 7
for sumi in range(1 , n + 1):
    for face in range(1 , 7):
        if face > sumi:
            continue
        dp[sumi] = (dp[sumi] + dp[sumi - face]) % mod
print(dp[n])