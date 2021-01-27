histograms = [
    [1, 3, 2, 1, 2],
    [1, 3, 5, 3, 2, 2, 3, 3, 1],
    [1, 3, 5, 3, 2, 2, 3, 3, 1, 0, 3, 6, 0, 3, 3],
    [6320, 6020, 6098, 1332, 7263, 672, 9472, 2838, 3401, 9494],
    [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116],
]

solutions = [5, 14, 14, 18060, 26152]


"""
areas = []
start = []

"""


def largest_rectangle(histogram):

    if len(histogram) == 0:
        return 0, [0]

    if len(histogram) == 1:
        return histogram[0], histogram

    areas = []
    histogram.append(0)
    start_coordinate = [0]
    heights = [histogram[0]]

    for position in range(1, len(histogram)):
        elem = histogram[position]

        if elem > heights[-1]:
            start_coordinate.append(position)
            heights.append(elem)

        elif elem < heights[-1]:
            starts_at = position
            while len(heights) > 0 and elem < heights[-1]:
                height = heights[-1]
                starts_at = start_coordinate[-1]

                del start_coordinate[-1]
                del heights[-1]

                areas.append(height * (position - starts_at))

            start_coordinate.append(starts_at)
            heights.append(elem)

    return max(areas), areas


for hist, sol in zip(histograms, solutions):
    max_area, areas = largest_rectangle(hist)
    print(f"Max area is: {max_area} , should be {sol},  all areas: {areas}")
    assert max_area == sol
