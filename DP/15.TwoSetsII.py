n = int(input())
sumi = (n * (n + 1)/2)
if sumi % 2: 
    print(0)
    exit()
sumi = int(sumi // 2)
dp = [0] * (sumi + 1)
mod = 10 ** 9 + 7
dp[0] = 1
for i in range(1 , n + 1):
    for targ in range(sumi , i - 1 ,-1):
        dp[targ] = (dp[targ] + dp[targ - i]) % mod
mod_inv_2 = pow(2, mod - 2, mod)
print((dp[sumi] * mod_inv_2) % mod)
