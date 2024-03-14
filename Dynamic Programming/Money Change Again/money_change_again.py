# python3
import math

def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    dp = [-1 for i in range(money+1)]
    dp[0] = 0
    arr = [1, 3, 4]
    def fn(money,dp):
        if money == 0:
            return 0
        mi=math.inf

        for i in arr:
            if money >= i:
                if dp[money-i]==-1:
                    dp[money-i] = fn(money-i, dp)
                mi= min(mi, 1 + dp[money-i])
        return mi
    return fn(money, dp)





if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
