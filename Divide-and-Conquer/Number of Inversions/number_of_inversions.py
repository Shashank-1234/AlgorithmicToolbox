# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] < a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge(a, b):
    result = []
    inv = 0

    while a and b:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
            inv += len(a)
    result += a or b
    return result, inv



def merge_sort(a):
    if len(a) == 1:
        return a, 0
    mid = len(a)//2
    left, left_inv = merge_sort(a[:mid])
    right, right_inv = merge_sort(a[mid:])

    merged, merged_inv = merge(left, right)
    return merged, merged_inv + left_inv + right_inv

def compute_inversions(a):
    i, j = merge_sort(a)
    return j


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions_naive(elements))
