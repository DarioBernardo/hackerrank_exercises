"""
MEDIUM
https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def find_mid(node):
    if node is None:
        return None

    slow = node
    fast = node
    prev = None

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if prev is not None:
        prev.next = None
    return slow


def merge_sort(start):
    if start is None:
        return None

    if start.next is None:
        return start

    mid = find_mid(start)
    start_sorted = merge_sort(start)
    mid_sorted = merge_sort(mid)

    head = None
    last = None

    while not (mid_sorted is None and start_sorted is None):
        if mid_sorted is None or (start_sorted is not None and mid_sorted.val > start_sorted.val):
            if head is None:
                head = start_sorted
                last = head
            else:
                last.next = start_sorted
                last = last.next

            start_sorted = start_sorted.next

        else:
            if head is None:
                head = mid_sorted
                last = head
            else:
                last.next = mid_sorted
                last = last.next

            mid_sorted = mid_sorted.next

    return head


class Solution:
    def sortList(self, head):
        if head is None:
            return head

        sorted_list = merge_sort(head)
        return sorted_list





