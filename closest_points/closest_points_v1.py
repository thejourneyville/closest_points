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


def divide_conquer_shortest_distance(coordinates_by_x):

    # base cases
    if len(coordinates_by_x) <= 1:
        return 0
    elif len(coordinates_by_x) == 2:
        return coordinates_by_x[0], coordinates_by_x[-1]
    elif len(coordinates_by_x) == 3:
        results = [(distance(coordinates_by_x[i], coordinates_by_x[(i + 1) % 3]),
                    coordinates_by_x[i], coordinates_by_x[(i + 1) % 3]) for i in range(3)]
        return min(results)[1:]

    # recursively divide and conquer each half of x coordinates
    else:
        middle = len(coordinates_by_x) // 2

        left = divide_conquer_shortest_distance(coordinates_by_x[:middle])
        right = divide_conquer_shortest_distance(coordinates_by_x[middle:])

        if distance(left[0], left[-1]) < distance(right[0], right[-1]):
            delta = left
        else:
            delta = right

        return delta









test_list = ((2, 2), # A
            (2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  )
sorted_x = merge_sort_generator(test_list, 0)
print(sorted_x)
print(divide_conquer_shortest_distance(sorted_x))