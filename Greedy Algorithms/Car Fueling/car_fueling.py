# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    n = len(stops)
    stops = [0]+stops+[d]
    curr_stop = 0
    number_of_fills = 0
    present_milage = m

    while curr_stop < n+1:
        dist = stops[curr_stop + 1] - stops[curr_stop]
        if dist > m:
            return -1
        if present_milage >= dist:
            present_milage = present_milage - dist
        else:
            present_milage = m - dist
            number_of_fills += 1
        curr_stop += 1
    return number_of_fills



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
