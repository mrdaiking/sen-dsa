"""
Day 22 - Merge Two Sorted Lists (Linked List Pattern)
Leetcode: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """Helper method to print the linked list"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

def mergeTwoLists(list1, list2):
    """
    Merge two sorted linked lists using iterative approach
    """
    dummy = ListNode() # create a dummy node to return the final merged list
    tail = dummy # create a tail pointer to build the merged list
    
    while list1 and list2: # iterate while both lists are not empty
        if list1.val < list2.val: # compare the values of the two lists
            tail.next = list1 # append the smaller value to the merged list
            list1 = list1.next # move the pointer of the list from which the node was taken
        else:
            tail.next = list2 # append the smaller value to the merged list
            list2 = list2.next # move the pointer of the list from which the node was taken
        tail = tail.next # move the tail pointer to the end of the merged list
    
    if list1: # if there are remaining nodes in list1, append them to the merged list
        tail.next = list1 # append the remaining nodes
    if list2: # if there are remaining nodes in list2, append them to the merged list
        tail.next = list2 # append the remaining nodes
    return dummy.next

def mergeTwoListsRecursive(list1, list2):
    """
    Merge two sorted linked lists using recursive approach
    """
    # TODO: Implement here (bonus)
    pass

# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to array
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([5], [1, 2, 4], [1, 2, 4, 5]),
        ([1, 2, 4], [5], [1, 2, 4, 5]),
        ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ]
    
    for i, (arr1, arr2, expected) in enumerate(test_cases):
        list1 = create_linked_list(arr1)
        list2 = create_linked_list(arr2)
        
        result = mergeTwoLists(list1, list2)
        result_array = linked_list_to_array(result)
        
        print(f"Test {i+1}: list1={arr1}, list2={arr2}")
        print(f"Output: {result_array}")
        print(f"Expected: {expected}")
        print(f"Pass: {result_array == expected}")
        print("-" * 50)