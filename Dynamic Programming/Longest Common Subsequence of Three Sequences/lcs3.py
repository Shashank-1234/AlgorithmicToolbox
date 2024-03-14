# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100
    dp= [[[-1 for k in range(len(third_sequence)+1)] for j in range(len(second_sequence)+1)]for i in range(len(first_sequence)+1)]
    def fn(a, b, c, i, j, k):
        c1, c2, c3, c4 = float('-inf'), float('-inf'), float('-inf'), float('-inf')
        if i == len(a) or j == len(b) or k == len(c):
            return 0
        if a[i] == b[j] == c[k]:
            if dp[i+1][j+1][k+1] == -1:
                dp[i+1][j+1][k+1] = fn(a, b, c, i + 1, j + 1, k + 1)
            c1 = 1 + dp[i+1][j+1][k+1]

        if dp[i + 1][j][k] == -1:
            dp[i + 1][j][k] = fn(a, b, c, i + 1, j, k)
        c2 = dp[i + 1][j][k]
        if dp[i][j + 1][k] == -1:
            dp[i][j + 1][k] = fn(a, b, c, i, j + 1, k)
        c3 = dp[i][j + 1][k]
        if dp[i][j][k + 1] == -1:
            dp[i][j][k + 1] = fn(a, b, c, i, j, k + 1)
        c4 = dp[i][j][k + 1]
        return max(c1, c2, c3, c4)
    return fn(first_sequence, second_sequence, third_sequence, 0, 0, 0)
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
