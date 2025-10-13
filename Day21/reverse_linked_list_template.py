
"""
Reverse Linked List - Template
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0]) # Create the head node
    curr = head # Pointer to track the current node
    for val in arr[1:]: # Start from the second element
        curr.next = ListNode(val) # Create a new node and link it
        curr = curr.next # Move to the new node
    return head

def print_linked_list(head):
    """
    Print linked list in a readable format.
    """
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(' -> '.join(vals))


def reverse_linked_list(head: ListNode):
    """
    Reverse a singly linked list (iterative).
    Returns new head.
    """
    prev = None
    curr = head
    while curr:
        next_node = curr.next # Store next node pointer
        curr.next = prev # Set current node's next to previous node
        prev = curr # Move previous pointer to current node
        curr = next_node # Move current pointer to next node
    return prev # New head of the reversed list

def reverse_linked_list_recursive(head: 'ListNode') -> 'ListNode':
    """
    Reverse a singly linked list using recursion.
    Returns new head.
    """
    if not head or not head.next:
        return head
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head   

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = build_linked_list(arr)
    print("Original:")
    print_linked_list(head)
    head = reverse_linked_list(head)
    print("Reversed:")
    print_linked_list(head)

    # Test recursive version
    head = build_linked_list(arr)
    head = reverse_linked_list_recursive(head)
    print("Reversed (recursive):")
    print_linked_list(head)
