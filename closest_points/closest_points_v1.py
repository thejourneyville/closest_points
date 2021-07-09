from sys import maxsize


# SORT ---------------------------
def merge_sort_generator(A, x):
    def merge_sort(a, start, end):

        def merge(segment, s, m, e):

            left = segment[s:m + 1] + [(maxsize, maxsize)]
            right = segment[m + 1:e + 1] + [(maxsize, maxsize)]

            i, j = 0, 0
            for idx in range(s, e + 1):
                if left[i][x] <= right[j][x]:
                    segment[idx] = left[i]
                    i += 1
                else:
                    segment[idx] = right[j]
                    j += 1
            return segment

        if start < end:
            mid = (start + end) // 2
            merge_sort(a, start, mid)
            merge_sort(a, mid + 1, end)
            merge(a, start, mid, end)

        return a

    return merge_sort(list(A), 0, len(A) - 1)


# --------------------------------


# DISTANCE -----------------------
def distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


# --------------------------------


# RECURSIVE FUNCTION -------------
def divide_conquer_shortest_distance(coordinates_by_x):

    # base cases
    points = len(coordinates_by_x)
    if points <= 3:
        if points <= 1:
            return 0
        elif points == 2:
            return distance(coordinates_by_x[0], coordinates_by_x[-1]), (coordinates_by_x[0], coordinates_by_x[-1])
        else:
            return merge_sort_generator([(distance(coordinates_by_x[idx], coordinates_by_x[(idx + 1) % 3]),
                                          (coordinates_by_x[idx], coordinates_by_x[(idx + 1) % 3])) for idx in
                                         range(3)], 0)[0]

    # this will repeat recursively until len(coordinates_by_x) <= 3:
    x_midpoint = points // 2
    x_leftside = divide_conquer_shortest_distance(coordinates_by_x[:x_midpoint])
    x_rightside = divide_conquer_shortest_distance(coordinates_by_x[x_midpoint:])

    # find delta: the shortest distance pair of left and right sides
    print(x_rightside)
    if x_leftside[0] < x_rightside[0]:
        delta = x_leftside
    else:
        delta = x_rightside


test_list = ((1, 2), (9, 11), (5, 20))
sorted_x = merge_sort_generator(test_list, 0)
print(sorted_x)
print(divide_conquer_shortest_distance(sorted_x))
