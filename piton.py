#!/usr/bin/python3
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def check_cycle(head: ListNode) -> int:
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return 1  # Hay un ciclo

    return 0  # No hay ciclo

