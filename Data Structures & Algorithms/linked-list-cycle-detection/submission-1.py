# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Use fast and slow pointer, one pointer goes two at a time
        #One goes one at a time
        fast = head
        slow = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next
            fast = fast.next

            if slow == fast:
                return True

        return False