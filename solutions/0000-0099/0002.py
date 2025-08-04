# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(
        self, l1 , l2 
    ):
        dummy = ListNode()
        carry, curr = 0, dummy
        while l1 or l2 or carry:
            print(l1.val)
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(s, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        print(print_linked_list(dummy))
        return dummy.next
    
def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Properly create linked lists
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sum_solution = Solution()
result = sum_solution.addTwoNumbers(l1, l2)
print_linked_list(result) 