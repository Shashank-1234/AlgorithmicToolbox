# python3
import math

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    dp = [[-1 for j in range(len(second_sequence)+1)] for i in range(len(first_sequence) +1)]
    def fn(a, b, i, j):

        c1, c2, c3 = float('-inf'), float('-inf'), float('-inf')
        if i == len(a) or j == len(b):
            return 0

        if a[i] == b[j]:
            if dp[i + 1][j + 1] == -1:
                dp[i + 1][j + 1] = fn(a, b, i + 1, j + 1)
            c3 = 1 + dp[i + 1][j + 1]

        if dp[i + 1][j] == -1:
            dp[i + 1][j] = fn(a, b, i + 1, j)
        c1 = dp[i + 1][j]

        if dp[i][j + 1] == -1:
            dp[i][j + 1] = fn(a, b, i, j + 1)
        c2 = dp[i][j + 1]

        return max(c1, c2, c3)
    return fn(first_sequence, second_sequence, 0, 0)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
