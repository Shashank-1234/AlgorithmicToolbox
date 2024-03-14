# python3
import math


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    dp = [[-1, []]] * (n + 1)
    dp[0] = [0, [0]]
    arr = []*(n+1)
    def fn(n,dp):
        c1, c2, c3 = math.inf, math.inf, math.inf
        if n <= 1:
            return 0, [0]
        if n > 1:
            if n % 3 == 0:
                if dp[n//3][0] == -1:
                    dp[n//3][0], dp[n//3][1] = fn(n//3, dp)
                c3, C3 = 1 + dp[n // 3][0], dp[n//3][1]+[n]

            elif n % 2 == 0:
                if dp[n//2][0] == -1:
                    dp[n//2][0], dp[n//2][1] = fn(n//2, dp)
                c2, C2 = 1 + dp[n//2][0], dp[n//2][1] + [n]
            else:
                if dp[n-1][0] == -1:
                    dp[n-1][0], dp[n-1][1] = fn(n-1, dp)
                c1,C1 = 1 + dp[n-1][0], dp[n-1][1]+[n]
        if c3 == min(c1, c2, c3):
            return c3, C3
        if c2 == min(c1, c2, c3):
            return c2, C2
        if c1 == min(c1, c2, c3):
            return c1, C1
    a, b = fn(n, dp)
    return b

if __name__ == '__main__':
    input_n = int(input())

    output_sequence = compute_operations(input_n)
    print(len(output_sequence))
    print(*output_sequence)

