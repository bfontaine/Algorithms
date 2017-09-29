#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# Dynamic Time Wraping
#
# Good explanation: https://www.youtube.com/watch?v=_K1OsqCicBY

def avg(xs):
    return sum(xs) / float(len(xs))

def dtw(series1, series2):
    """
    Compute a distance between two numerical series using the DTW algorithm.
    """
    w = len(series1)
    h = len(series2)

    matrix = []
    for _ in range(h):
        l = [0]*w
        matrix.append(l)

    for x in range(w):
        for y in range(h):
            v1 = series1[x]
            v2 = series2[y]

            d = abs(v1 - v2)

            candidates = [0]
            if x > 0:
                candidates.append(matrix[y][x-1])

            if y > 0:
                candidates.append(matrix[y-1][x])

            if x > 0 and y > 0:
                candidates.append(matrix[y-1][x-1])

            matrix[y][x] = d + min(candidates)

    distances = []
    x = 0
    y = 0
    while x < w or y < h:
        distances.append(matrix[y][x])
        candidates = []
        if x+1 < w:
            candidates.append((x+1, y))

        if y+1 < h:
            candidates.append((x, y+1))

        if x+1 < w and y+1 < h:
            candidates.append((x+1, y+1))

        if not candidates:
            break

        min_distance = None
        for next_x, next_y in candidates:
            d = matrix[next_y][next_x]
            if min_distance is None or d < min_distance:
                min_distance = d
                x = next_x
                y = next_y

    return avg(distances)


def euclid(series1, series2):
    """
    Compute a distance between two numerical series using Euclidian distances
    between their points at the same index.
    """
    ds = [abs(series1[i] - series2[i])
            for i in range(min(len(series1), len(series2)))]
    return avg(ds)

def main():
    signal = [1, 5, 9, -3, -2, -2, 3, 12, 8, 9, 3]

    s1 = [0] * 4 + signal + [0] * 10
    s2 = [0] * 9 + signal + [0] * 1

    print("Euclid: %d" % euclid(s1, s2))
    print("DTW:    %d" % dtw(s1, s2))

if __name__ == "__main__":
    main()
