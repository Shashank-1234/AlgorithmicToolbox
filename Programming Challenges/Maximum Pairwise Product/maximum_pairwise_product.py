# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    max_index1, max_index2 = 0, 0
    for i, val in enumerate(numbers):
        if int(numbers[i]) > int(numbers[max_index1]):
            max_index1 = i

    if max_index1 == 0:
        max_index2 = 1
    else:
        max_index2 = 0

        # find the second highest number
    for j, val in enumerate(numbers):
        if j != max_index1 and int(numbers[j]) > int(numbers[max_index2]):
            max_index2 = j

    return int(numbers[max_index1]) * int(numbers[max_index2])


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
