from typing import List


def check_shift(a: str, b: str) -> bool:
    offset = None
    for ca, cb in zip(a, b):
        if offset is None:
            offset = ord(ca) - ord(cb)
        else:
            if offset != ord(ca) - ord(cb):
                return False

    return True


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        if len(strings) == 0:
            return []

        groups = dict()
        for elem in strings:
            group_list = groups.get(len(elem), [])
            group_list.append(elem)
            groups[len(elem)] = group_list

        sol = []
        for str_group_len, group_list in groups.items():
            group_sol = dict()
            for elem in group_list:
                if len(group_sol) == 0:
                    group_sol[elem] = [elem]
                else:
                    group = elem
                    for possible_group, group_list in group_sol.items():
                        if check_shift(possible_group, elem):
                            group = possible_group

                    the_group = group_sol.get(group, [])
                    the_group.append(elem)
                    group_sol[group] = the_group

            sol.extend(list(group_sol.values()))

        return sol


din = [
    ["abc","bcd","acef","xyz","az","ba","a","z"]
]

expected_out = [
    [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
]

for i, expected in zip(din, expected_out):
    s = Solution()
    actual = s.groupStrings(i)
    print(actual)
    print(expected)
    assert actual == expected