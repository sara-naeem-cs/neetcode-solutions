# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        i = 0
        while curr:
            i = i + 1
            curr = curr.next
        
        #Position of the node to delete is (i-n+1)

        curr = head
        prev = None
        j = 0
        node_position = i-n

        if node_position == 0:
            return head.next

        while curr:
            #When deleting
            #previous.next = curr.next

            if j == node_position:
                #delete this node
                prev.next = curr.next
                break
            else:
                j = j + 1
                prev = curr
                curr = curr.next


        return head
