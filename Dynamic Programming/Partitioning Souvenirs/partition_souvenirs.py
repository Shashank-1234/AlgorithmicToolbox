from itertools import product
from sys import stdin


def partition3_naive(values):
    for c in product(range(3), repeat=len(values)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
    dp = {}
    a, b, c = 0,0,0
    n=len(values)
    def fn(arr, a, b, c, i):
        t = str(a) + "-" + str(b) + str(c)
        if i == n:
            if a == b and b == c:
                return 1
            return 0
        if t in dp:
            return dp[t]

        c1 = fn(arr, a+arr[i], b, c, i+1)
        c2 = fn(arr, a, b +arr[i], c, i + 1)
        c3 = fn(arr, a, b, c + arr[i], i + 1)

        dp[t] = max(c1, c2, c3)
        return dp[t]
    return fn(values, 0, 0, 0, 0)


if __name__ == '__main__':
    input_n =int(input())
    input_values = list(map(int, input().split()))

    assert input_n == len(input_values)
    print(partition3(input_values))

