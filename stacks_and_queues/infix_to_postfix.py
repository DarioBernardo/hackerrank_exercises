"""
Exercise:
https://www.geeksforgeeks.org/convert-infix-prefix-notation/

Infix and postfix notation explained well at: http://www.cs.man.ac.uk/~pjj/cs212/fix.html
"""
from typing import List

sin = [
    "A * B + C / D".split(" "),
    "( A - B / C ) * ( A / K - L )".split(" "),
    "A * ( B + C ) / D".split(" ")
]
sout = [
    "+ * A B / C D",
    "* - A / B C - / A K L",
    "* A / + B C D"  # "/ * A + B C D" also works
]

"""
operands = []
operators = []

res = []
"""


def infix_to_prefix(arr: List[str]) -> List[str]:
    operands = []
    operators = []

    operators_list = ["+", "*", "/", "-", "(", ")"]
    high_priority_operands = ["*", "/", "("]

    def create_op(nds, ors):
        op = ors.pop()
        second_operand = nds.pop()
        first_operand = nds.pop()
        operation = f"{op} {first_operand} {second_operand}"
        nds.append(operation)

    """
    position = 3
    elem = C
    operands = [A, + B C]
    operators = [*, (,]
    """
    for position, elem in enumerate(arr):  # A * ( B + C ) / D
        if elem not in operators_list:
            if len(operands) == 0:
                operands.append(elem)
            else:
                if len(operators) > 0 and operators[-1] in ["*", "/"]:
                    operands.append(elem)
                    create_op(operands, operators)

                elif position+1 < len(arr) and arr[position+1] not in high_priority_operands or position+1 >= len(arr):
                    operands.append(elem)
                    if operators[-1] != '(':
                        create_op(operands, operators)
                elif position+1 < len(arr) and arr[position+1] in high_priority_operands:
                    operands.append(elem)

        else:
            if elem is ")":
                if len(operators) < 1:
                    raise Exception("maybe missing `(` ?")
                while operators[-1] != "(":
                    create_op(operands, operators)

                del operators[-1]
            else:
                operators.append(elem)

    while len(operators) > 0:
        create_op(operands, operators)

    return operands[0]


for i, expected in zip(sin, sout):
    actual = infix_to_prefix(i)
    print(f"Actual: \t{actual}\nExpected:\t{expected}")
    assert actual == expected
