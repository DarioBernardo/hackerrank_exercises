"""
Stable Marriage

Given N men and N women and the marriage preference order for each man and woman.
Their marriage will be stable when these men and women marry in such a manner so that everyone gets the most desired
partner as per the availability( partners in a marriage cannot find anyone else better than what they get).

Wiki Definition- Given n men and n women, where each person has ranked all members of the opposite sex in order
of preference, marry the men and women together such that there are no two people of the opposite sex who would
both rather have each other than their current partners. When there are no such pairs of people,
the set of marriages is deemed stable.

https://algorithms.tutorialhorizon.com/stable-marriage-problem-gale-shapley-algorithm-java/
"""

men = [4, 5, 3, 6, 8, 9, 10]
women = [2, 5, 6, 9, 10, 8, 11]


def get_next_proposal(prop_map):

    for stag, women_to_propose in prop_map.items():
        if len(women_to_propose) > 0:
            break

    if len(women_to_propose) == 0:
        return None, None

    bride = women_to_propose.pop(0)
    prop_map[stag] = women_to_propose
    return stag, bride


def stable_matching(m, w) -> list:
    pairs = {}
    proposition_map = {}
    free_woman = set()
    for woman in w:
        free_woman.add(woman)

    for man in m:
        proposition_map[man] = women.copy()

    while True:
        stag, bride = get_next_proposal(proposition_map)
        if not stag or not bride:
            break

        new_couple = (stag, bride)
        if bride in free_woman:
            print(f"man {stag} engaged with {bride}")
            free_woman.discard(bride)
            pairs[bride] = new_couple

        else:
            other_couple = pairs[bride]
            if other_couple[0] < new_couple[0]:
                print(f"NEW COUPLE: man {new_couple[0]} engaged with {bride} rather than {other_couple[0]}")
                pairs[bride] = new_couple
                m.append(other_couple[0])

    result = []
    for w, couple in pairs.items():
        result.append(couple)

    return result


res = stable_matching(men, women)
print(res)
print(men)
