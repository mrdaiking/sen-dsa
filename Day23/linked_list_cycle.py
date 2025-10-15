"""
Day 23 - Linked List Cycle (Floyd’s Tortoise and Hare)
Leetcode: https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Return True if there is a cycle in the linked list. Otherwise, return False.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: True

Example 2:
Input: head = [1,2], pos = 0
Output: True

Example 3:
Input: head = [1], pos = -1
Output: False

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode):
    """
    Detect cycle in linked list using Floyd’s Tortoise and Hare algorithm
    """
    slow = fast = head
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False

# Helper to create linked list with cycle for testing
def create_linked_list_with_cycle(arr, pos):
    if not arr:
        return None
    nodes = [ListNode(val) for val in arr]
    for i in range(len(arr) - 1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Test cases
if __name__ == "__main__":
    tests = [
        ([3,2,0,-4], 1, True),
        ([1,2], 0, True),
        ([1], -1, False),
        ([1,2,3,4,5], -1, False),
        ([1,2,3,4,5], 2, True),
        ([], -1, False),
    ]
    for arr, pos, expected in tests:
        head = create_linked_list_with_cycle(arr, pos)
        result = hasCycle(head)
        print(f"Input: {arr}, pos={pos} | Output: {result} | Expected: {expected}")
