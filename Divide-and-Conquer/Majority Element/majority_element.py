# python3
from sqlalchemy.ext.indexable import index_property


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def first(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if (arr[mid] == x):
            if (mid-1 >= 0 and arr[mid-1] == x) :
                high = mid-1
                continue

            return mid
        elif (x > arr[mid]):
            return first(arr, (mid + 1), high, x)
        else:
            return first(arr, low, (mid - 1), x)

def last(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if (arr[mid] == x) :
            if (mid+1 < len(arr) and arr[mid+1] == x) :
                low = mid + 1
                continue
            return mid
        elif (x > arr[mid]):
            return last(arr, (mid + 1), high, x)
        else:
            return last(arr, low, (mid - 1), x)

def majority_element1(elements):
    assert len(elements) <= 10 ** 5

    elements = sorted(elements)
    n = len(elements)
    elements1 = list(set(elements))
    for ele in elements1:
        num = last(sorted(elements), 0, n - 1, ele) - first(sorted(elements), 0, n - 1, ele)
        if num >= n // 2:
            return 1
    return 0

def majority_element(elements):
    assert len(elements) <= 10 ** 5
    elements = sorted(elements)

    candidate = -1
    votes = 0
    n = len(elements)
    for i in range(n):
        if votes == 0:
            candidate = elements[i]
            votes = 1
        else:
            if elements[i] == candidate:
                votes += 1
            else:
                votes -= 1

    count = 0
    for i in range(n):
        if elements[i] == candidate:
            count += 1
    if count > n/2:
        return 1
    return 0
    

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
