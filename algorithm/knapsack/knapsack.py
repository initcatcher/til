v = [10, 40, 30, 50]
w = [5, 4, 6, 3]
W = 10


def knapsack(v, w, W):
    n = len(v)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


print(knapsack(v, w, W))


def knapsack_v2(v, w, W):
    n = len(v)
    dp = [0] * (W + 1)

    for i in range(n):
        for j in range(W, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    return dp[W]


print(knapsack_v2(v, w, W))
