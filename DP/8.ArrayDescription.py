n , m = map(int , input().split())
arr = list(map(int , input().split()))
dp = [[0 for _ in range(m + 1)] for _ in range(n)]
for ele in arr:
    if ele == 0:
        for i in range(n):
            dp[]
