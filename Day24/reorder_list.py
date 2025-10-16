class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: ListNode):
    if not head or not head.next:
        return head
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse the second half
    second = slow.next
    slow.next = None
    second = reverse_linked_list(second)
    # Merge two halves
    first = head
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
    return head

# Optional: Helper functions for testing

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(' -> '.join(res))

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# Example usage:
if __name__ == "__main__":
    head = build_linked_list([1,2,3,4,5])
    reorderList(head)
    print_linked_list(head)
