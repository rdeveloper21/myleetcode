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
            print(l1)
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(s, 10)
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
l1= ListNode(2)
l1.next = 4
l1.next = 3
l2 = ListNode(5)
l2.next = 6
l2.next = 4
# print(l1.val)
sum = Solution()
sum.addTwoNumbers(l1, l2)