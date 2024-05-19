from math import ceil


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_count = 0

        temp_head = head
        while temp_head.next is not None:
            temp_head = temp_head.next
            nodes_count += 1

        middle_node_num = ceil(nodes_count / 2)
        middle_node = head

        for i in range(middle_node_num):
            middle_node = middle_node.next

        return middle_node

    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     slow_pointer = head
    #     fast_pointer = head
    #
    #     while fast_pointer is not None and fast_pointer.next is not None:
    #         slow_pointer = slow_pointer.next
    #         fast_pointer = fast_pointer.next.next
    #
    #     return slow_pointer
