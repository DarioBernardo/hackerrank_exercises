# Find all possible combination of friends using recursion

from itertools import combinations


friends = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M']
# friends = ['A', 'B', 'C', 'D']
table_size = 5

# print([tuple(elem) for elem in friends])
solution = [x for x in combinations(friends, table_size)]
print(solution)


def get_table_guest(friends_list, table_size, group=[], groups=[]):

    if len(group) is table_size:
        groups.append(tuple(group))
        return

    if len(group) + len(friends_list) == table_size:
        group.extend(friends_list)
        groups.append(tuple(group))
        return

    curr_friend = friends_list.pop(0)
    group_without = group.copy()
    group.append(curr_friend)

    # take branch
    get_table_guest(friends_list.copy(), table_size, group, groups)

    # leave branch
    get_table_guest(friends_list.copy(), table_size, group_without, groups)

    return groups


prop_solution = get_table_guest(friends, table_size)
print(prop_solution)

for elem in solution:
    if elem in prop_solution:
        prop_solution.remove(elem)
    else:
        raise Exception(f"Element {elem} not present")

if len(prop_solution) >0:
    raise Exception(f"There are some extra elements in the proposed solution: {prop_solution}")

if len(prop_solution) == 0:
    print("ALL GOOD!")