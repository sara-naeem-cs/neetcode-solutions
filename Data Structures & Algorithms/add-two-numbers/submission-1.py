# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 and curr2:
            added_val = curr1.val + curr2.val
            #We're going to add them and edit l1
            if (added_val - 10) > 0:
                carry = 1
                added_val = added_val - 10
            else:
                carry = 0
            
            curr1.val = added_val


            if curr1.next == None and curr2.next == None:
                if carry > 0:
                    node = ListNode(carry)
                    node.next = None
                    curr1.next = node
                    break
            elif curr1.next == None:
                curr1.next = curr2.next
                break
            elif curr2.next == None:
                curr2.next = curr1.next
                break

            
            curr1 = curr1.next
            curr2 = curr2.next







        return l1