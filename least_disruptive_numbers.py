import random

original = [random.randint(-10, 100) for x in range(0, 100)]
replacement = [random.randint(-10, 100) for _ in range(0, 5)]

print(original)
print(replacement)


def calculate_cost(orig, repl):
    if len(orig) != len(repl):
        raise Exception(f"The two list segments have different length: {len(orig)} {len(repl)}")

    return sum([a_i - b_i for a_i, b_i in zip(orig, repl)])


replacement_cost = []
for i in range(0, len(original)-len(replacement)):
    sub_original = original[i:i+len(replacement)]
    replacement_cost.append(abs(calculate_cost(sub_original, replacement)))


index_of_min = replacement_cost.index(min(replacement_cost))

print(f"Cost list: {replacement_cost}")
print(f"Min cost: {min(replacement_cost)}")
print(f"Cost index: {index_of_min}")
