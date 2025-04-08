arr = [10, 20, 10, 30, 20, 50]
n = len(arr)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # 결과: 4


import bisect

arr = [10, 20, 10, 30, 20, 50]
dp = []

for num in arr:
    idx = bisect.bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))  # 결과: 4
