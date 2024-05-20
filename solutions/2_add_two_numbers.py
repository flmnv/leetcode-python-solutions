# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(0)
        result_pointer = result_head
        rest = 0

        while l1 or l2 or rest:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sum_ = val1 + val2 + rest
            rest = sum_ // 10

            result_pointer.next = ListNode(sum_ % 10)
            result_pointer = result_pointer.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result_head.next
