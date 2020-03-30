histograms = [
    [1, 3, 2, 1, 2],
    [1, 3, 5, 3, 2, 2, 3, 3, 1],
    [1, 3, 5, 3, 2, 2, 3, 3, 1, 0, 3, 6, 0, 3, 3]
]

solutions = [5, 14, 14]


def largest_rectangle(histogram):
    stack = []
    pos = []
    areas = []
    max_area = -1

    for i, elem in enumerate(histogram):
        new_hist_start = i
        while len(stack) > 0 and elem < stack[-1]:
            histo_start = pos.pop()
            height = stack.pop()
            base = i - histo_start
            area = height * base
            areas.append(area)
            max_area = max(max_area, area)

            new_hist_start = histo_start

        if len(stack) > 0 and elem > stack[-1] or len(stack) == 0:
            stack.append(elem)
            pos.append(new_hist_start)

    # Flush end of the stack
    while len(stack) > 0:
        histo_start = pos.pop()
        height = stack.pop()
        base = len(histogram) - histo_start
        area = height * base
        areas.append(area)
        max_area = max(max_area, area)

    return max_area, areas


for hist, sol in zip(histograms, solutions):
    max_area, areas = largest_rectangle(hist)
    print(f"Max area is: {max_area} , should be {sol},  all areas: {areas}")
    assert max_area == sol
