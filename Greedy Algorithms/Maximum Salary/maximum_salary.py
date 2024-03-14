# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    if len(numbers) == 1:
        return numbers[0]

    num_str = [str(num) for num in numbers]
    num_str.sort(key=lambda x: x, reverse=True)
    return int(''.join(num_str))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
