# python3
import math

def edit_distance(first_string, second_string):
    dp = [[-1 for j in range(len(second_string) +1)] for i in range(len(first_string) +1)]

    def fn(a, b, i, j, dp):
        c1, c2, c3, c4 = math.inf, math.inf, math.inf, math.inf
        if i == len(a) or j == len(b):
            return abs((len(a)-i)-(len(b)-j))
        if a[i] == b[j]:
            if dp[i+1][j+1] == -1:
                dp[i+1][j+1] = fn(a, b, i+1, j+1, dp)
            c3 = dp[i+1][j+1]
        else:
            if dp[i+1][j+1] == -1:
                dp[i+1][j+1] = fn(a, b, i+1, j+1, dp)
            c4 = 1 + dp[i+1][j+1]

            if dp[i+1][j] == -1:
                dp[i+1][j] = fn(a, b, i+1, j, dp)
            c1 = 1 + dp[i+1][j]

            if dp[i][j+1] == -1:
                dp[i][j+1] = fn(a, b, i, j+1, dp)
            c2 = 1 + dp[i][j+1]

        return min(c1, c2, c3, c4)
    return fn(first_string, second_string, 0, 0, dp)


if __name__ == "__main__":
    print(edit_distance(input(), input()))
