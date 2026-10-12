class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def kNodesChecker(node):
            i = 0
            while node != None and i < k:
                i += 1
                node = node.next
            return i == k

        dummy = ListNode(0, None)
        dummy.next = head
        groupPrevTail = dummy

        while kNodesChecker(groupPrevTail.next):
            prev = None
            curr = groupPrevTail.next
            groupNewTail = curr          # original first node = will become tail

            for _ in range(k):           # reverse exactly k nodes
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # prev is now the new head of this reversed group
            # curr is now the node right after this group (unprocessed)
            # groupNewTail is the original first node (now the tail)

            groupPrevTail.next = prev        # connect previous group to new head
            groupNewTail.next = curr          # connect new tail to next unprocessed node

            groupPrevTail = groupNewTail      # advance for next iteration

        return dummy.next