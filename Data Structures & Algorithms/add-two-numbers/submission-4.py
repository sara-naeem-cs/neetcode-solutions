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
        newList = ListNode() #this stores the head of the list
        curr = newList #this will be iterator for our list

        while curr1 or curr2:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            added_val = curr1.val + curr2.val + carry
            #We're going to add them and edit l1
            if added_val >= 10:
                carry = 1
                added_val = added_val - 10
            else:
                carry = 0
            
            curr.next = ListNode(added_val)

            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next
       
        if carry > 0:
            curr.next = ListNode(carry)



        return newList.next