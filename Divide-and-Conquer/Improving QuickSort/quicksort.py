# python3

from random import randint


def partition3(array, left, right):
    b = left
    for i in range(left+1, right+1):
        if array[i] <= array[left]:
            array[b+1], array[i] = array[i], array[b+1]
            b += 1
    array[left], array[b] = array[b], array[left]

    a = left
    for i in range(left, b):
        if array[i] < array[b]:

            a += 1
            array[a], array[i] = array[i], array[a]
    return a, b



def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    """make a call to partition3 and then two recursive calls 
to randomized_quick_sort"""
    a, b = partition3(array, left, right)

    randomized_quick_sort(array, left, a)
    randomized_quick_sort(array, b+1, right)



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
