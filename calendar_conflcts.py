calendars = [
    [
        [1, 2, 'a'],
        [3, 5, 'b'],
        [4, 6, 'c'],
        [7, 10, 'd'],
        [8, 11, 'e'],
        [13, 14, 'g'],
        [15, 16, 'h'],
    ],
    [
        [1, 2, 'a'],
        [3, 5, 'b'],
        [4, 6, 'c'],
        [7, 11, 'd'],
        [8, 12, 'e'],
        [10, 12, 'f'],
        [13, 14, 'g'],
        [13, 14, 'h'],
    ],
    [
        [1, 2, 'a'],
        [3, 5, 'b'],
        [4, 6, 'c'],
        [7, 9, 'd'],
        [8, 11, 'e'],
        [10, 12, 'f'],
        [13, 14, 'g'],
        [13, 14, 'h'],
        [15, 16, 'i'],
    ],
    [
        [1, 2, 'a'],
        [3, 5, 'b'],
        [4, 6, 'c'],
        [7, 10, 'd'],
        [8, 12, 'e'],
        [9, 14, 'f'],
        [13, 15, 'g'],
        [16, 17, 'h'],
        [18, 19, 'i'],
        [18, 19, 'l'],
        [18, 20, 'm'],
    ]
]

solutions = [
    [['b', 'c'], ['d', 'e']],
    [['b', 'c'], ['d', 'e', 'f'], ['g', 'h']],
    [['b', 'c'], ['d', 'e', 'f'], ['g', 'h']],
    [['b', 'c'], ['d', 'e', 'f', 'g'], ['i', 'l', 'm']],
]



def find_conflicts(cal):
    start_times_stack = []
    end_times_stack = []
    calendar_event_names = []

    conflicts = []

    for event in cal:
        if len(start_times_stack) != 0:
            # check end this event start time is after or before stacked event end times
            if end_times_stack[len(end_times_stack)-1] < event[0]:
                # no conflicts here. Pop everything
                current_conflict = []
                for i in range(0, len(end_times_stack)):
                    current_conflict.append(calendar_event_names.pop(0))
                    _ = start_times_stack.pop(0)
                    _ = end_times_stack.pop(0)

                if len(current_conflict) > 1:
                    conflicts.append(current_conflict)

        start_times_stack.append(event[0])
        end_times_stack.append(event[1])
        calendar_event_names.append(event[2])

    if len(start_times_stack) > 1:
        current_conflict = []
        for i in range(0, len(end_times_stack)):
            current_conflict.append(calendar_event_names.pop(0))
            _ = start_times_stack.pop(0)
            _ = end_times_stack.pop(0)

        conflicts.append(current_conflict)

    return conflicts


for calendar, solution in zip(calendars, solutions):
    my_sol = find_conflicts(calendar)
    print(my_sol)
    # print(solution)
    assert my_sol == solution

print("DONE!")
