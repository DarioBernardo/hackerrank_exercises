
# Add any extra import statements you may need here
ALLOWED_ELEMS = "{ [ ( ) ] }".split(" ")
OPENING = "{ [ (".split(" ")
CLOSING = ") ] }".split(" ")


def check_valid(c):
    if c not in ALLOWED_ELEMS:
        raise Exception("bla bla")


def check_matching(a, b):
    if b == ')':
        return a == '('

    if b == ']':
        return a == '['

    if b == '}':
        return a == '{'

# Add any helper functions you may need here


def is_balanced(s):
    # Write your code here

    stack = []

    for c in s:
        check_valid(c)

        if c in OPENING:
            stack.append(c)
        elif c in CLOSING:  # Checking if it is in closing is redundant but safer
            if len(stack) == 0:
                return False

            last_elem = stack.pop()
            if not check_matching(last_elem, c):
                return False

    if len(stack) > 0:
        return False

    return True


din = ['{[()]}', '{}()', '{(})', ')', "{[(])}", "{{[[(())]]}}", '(']
dout = [True, True, False, False, False, True, False]

for data_in, expected_result in zip(din, dout):
    actual_result = is_balanced(data_in)
    print(f"Expected: {expected_result}   Actual: {actual_result}")
    assert expected_result == actual_result
