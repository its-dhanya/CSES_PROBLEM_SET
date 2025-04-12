import bisect
n = int(input())
arr = list(map(int , input().split()))
ans =  []
for num in arr:
    ind = bisect.bisect_left(ans ,  num)
    if ind == len(ans):
        ans.append(num)
    else:
        ans[ind] = num
print(len(ans))