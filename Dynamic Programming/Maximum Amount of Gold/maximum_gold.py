# python3

from sys import stdin


def maximum_gold(capacity, arr):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(arr) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in arr)
    dp = [[-1 for j in range(capacity+1)] for i in range(len(arr)+1)]
    def fn(w, i,):
        c1, c2 = float('-inf'), float('-inf')
        if i == len(arr):
            return 0

        if w >= arr[i]:
            if dp[i+1][w-arr[i]] == -1:
                dp[i+1][w-arr[i]] = fn(w-arr[i], i+1)

            c1 = arr[i] + dp[i+1][w-arr[i]]
        if dp[i + 1][w] == -1:
            dp[i + 1][w] = fn(w, i+1)
        c2 = dp[i + 1][w]
        return max(c1, c2)
    return fn(capacity, 0)


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
