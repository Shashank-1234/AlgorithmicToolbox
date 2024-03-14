# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

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
    if n > len(curr):
        return ((sum(curr) * (n // len(curr))) + sum(curr[: (n+1) % len(curr)])) % 10
    else:
        return sum(curr) % 10




if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
