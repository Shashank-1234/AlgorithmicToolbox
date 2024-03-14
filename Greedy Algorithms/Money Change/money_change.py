# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    total = 0
    lst = [1, 5, 10]
    l = len(lst)
    for i in range(l):
        c = money // lst[-i-1]
        total += c
        money -= c * lst[-i-1]
    return total


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
