# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(m, n):
    assert 0 <= m <= n <= 10 ** 18

    if n <= 1:
        return n
    curr = [0, 1]
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        if (previous == 0 and current == 1):
            break

        curr.append(current)
    if (previous == 0 and current == 1):
        curr.pop()


    if n >= len(curr):
        N = (n+1) % len(curr)
    else:
        N = n+1
    return ((sum(curr) * (n // len(curr))) - (sum(curr) * (m // len(curr))) - sum(curr[:(m) % len(curr)]) + sum(curr[:N])) % 10



if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
