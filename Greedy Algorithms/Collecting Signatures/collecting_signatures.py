# python3

from collections import namedtuple
from sys import stdin
import math
Segment = namedtuple('Segment', 'start end')

def fun(s):
    a=[[-math.inf,math.inf]]
    c=1
    for i in s:
        b=0
        for j in range(c):
            x = max(i[0], a[j][0])
            y = min(i[1], a[j][1])
            if x <= y:
                a[j][0] = x
                a[j][1] = y
                b=1
                break
        if b==0:
            a.append([i[0],i[1]])
            c+=1
    return c





def compute_optimal_points(segments):

    sorted_seg = sorted(segments, key=lambda x: x.end)

    points = []
    while sorted_seg:
        segment = sorted_seg.pop(0)
        point = segment.end
        points.append(point)

        for s in sorted_seg[:]:
            if s.start <= point <= s.end:
                sorted_seg.remove(s)
    return points


if __name__ == '__main__':
    n = int(input())
    input_segments=[]
    for i in range(n):
        input_segments.append(list(map(int,input().split())))

    #input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    #output_points = compute_optimal_points(input_segments)
    #print(len(output_points))
    #print(*output_points)
    print(fun(input_segments))
