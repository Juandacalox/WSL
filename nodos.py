#!/usr/bin/python3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  

print(check_cycle(node1))


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None


print(check_cycle(node1))  

