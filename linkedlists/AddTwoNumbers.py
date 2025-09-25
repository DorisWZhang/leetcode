class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 2025-09-25
        # move through linkedlists adding nodes and tracking carry
        carry = 0
        head = ListNode() # placeholder node
        curr = head

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None: 
                currSum = l1.val + l2.val + carry
                carry = 0 # reset carry
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                currSum = l1.val + carry
                carry = 0
                l1 = l1.next
            else:
                currSum = l2.val + carry
                carry = 0
                l2 = l2.next
            if currSum > 9:
                carry = 1
                currSum %= 10
            curr.next = ListNode(currSum)
            curr = curr.next
        # if there is left over carry
        if carry == 1:
            curr.next = ListNode(carry)
        return head.next
