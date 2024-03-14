# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    j  = 1
    while j*(j+1) / 2 < n:
        summands.append(j)
        j += 1
    while True:
        temp = n - sum(summands)
        if temp not in summands:
            summands.append(temp)
            break
        else:
            summands.pop()

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
