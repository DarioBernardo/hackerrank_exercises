"""
https://leetcode.com/explore/interview/card/facebook/6/linked-list/3021/  (HARD)

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]


Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    if not head:
        return

    if not head.next:
        return

    # STEP 1: find middle point
    # STEP 2: reverse second part
    # STEP 3: stitch them togheter

    # STEP 1:
    slow_pointer = head
    fast_pointer = head
    while fast_pointer.next and fast_pointer.next.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    # STEP 2:
    prev = None
    current = slow_pointer.next  # in current I will find the beginning of the reversed list
    slow_pointer.next = None
    next_elem = current.next
    while next_elem:
        current.next = prev
        temp = next_elem.next
        prev = current
        current = next_elem
        next_elem = temp

    current.next = prev

    # STEP 3:
    pointer = head

    while current:
        temp_reverse = current.next
        temp_forwad = pointer.next
        pointer.next = current
        current.next = temp_forwad
        current = temp_reverse
        pointer = temp_forwad


din = [
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5]
]

dout = [
    [1, 4, 2, 3],
    [1, 5, 2, 4, 3]
]

for data_in, expected in zip(din, dout):
    head = None
    pointer = None
    for val in data_in:
        node = ListNode(val)
        if pointer:
            pointer.next = node
        pointer = node
        if not head:
            head = node

    reorderList(head)

    pointer = head
    counter = 0
    while pointer:
        print(pointer.val)
        assert pointer.val == expected[counter], "value {} do not match expected {}".format(pointer.val, expected[counter])
        counter += 1
        pointer = pointer.next

    assert counter == len(expected), "Different number of element returned!"
