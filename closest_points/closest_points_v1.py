import random

def closest_pair(A):
    # MERGE SORT ---------------------
    def merge_sort_generator(A, x):
        maxsize = 9223372036854775807

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
        num_of_points_x = len(coordinates_by_x)
        if num_of_points_x <= 3:
            if num_of_points_x <= 1:
                return 0
            elif num_of_points_x == 2:
                return distance(coordinates_by_x[0], coordinates_by_x[-1]), (coordinates_by_x[0], coordinates_by_x[-1])
            else:
                return merge_sort_generator([(distance(coordinates_by_x[idx], coordinates_by_x[(idx + 1) % 3]),
                                              (coordinates_by_x[idx], coordinates_by_x[(idx + 1) % 3])) for idx in
                                             range(3)], 0)[0]

        # this will repeat through to the end recursively until len(coordinates_by_x) <= 3:
        x_midpoint = num_of_points_x // 2
        x_leftside = divide_conquer_shortest_distance(coordinates_by_x[:x_midpoint])
        x_rightside = divide_conquer_shortest_distance(coordinates_by_x[x_midpoint:])

        # find delta: the shortest distance pair of left and right sides
        delta = x_leftside if x_leftside[0] < x_rightside[0] else x_rightside

        # find all pairs on either side of the center line (x_midpoint) which are < delta
        crossover_candidates = [point for point in coordinates_by_x if
                                abs(point[0] - coordinates_by_x[x_midpoint][0]) < delta[0]]

        # now sort the remaining candidates by their y-axis:
        coordinates_by_y = merge_sort_generator(crossover_candidates, 1)
        num_of_points_y = len(coordinates_by_y)

        # step through each point of the Y sorted list and check it's distance to another point at max 7 steps away
        for point_a in range(num_of_points_y - 1):
            counter = 1
            while counter < min((num_of_points_y - point_a), 7):
                distance_y = distance(coordinates_by_y[point_a], coordinates_by_y[point_a + counter])
                if distance_y < delta[0]:
                    delta = distance_y, (coordinates_by_y[point_a], coordinates_by_y[point_a + counter])
                else:
                    counter += 1

        return delta

    # --------------------------------

    return divide_conquer_shortest_distance(merge_sort_generator(A,0))[-1]



size = 40
population = 10

coords = [random.sample(range(size), 2) for _ in range(population)]

for point in range(population):
    for axis in range(2):
        coords[point][axis] = coords[point][axis] + (random.randint(0,9) * .1)
    coords[point] = tuple(coords[point])
coords = tuple(coords)

outer, inner = [], []
for row in range(size):
    for col in range(size):
        inner.append("     ")
    outer.append(inner)
    inner = []

for idx, xy in enumerate(coords):
    outer[round(xy[-1])][round(xy[0])] = f"{round(xy[0], 2)},{round(xy[-1], 2)}"

for row in range(len(outer)- 1, -1, -1):
    print(" ".join(outer[row]))

# print(divide_conquer_shortest_distance(sorted_x)[-1])
print(closest_pair(coords))