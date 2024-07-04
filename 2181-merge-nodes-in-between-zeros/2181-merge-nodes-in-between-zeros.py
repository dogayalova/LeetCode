# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # Initialize the dummy node and the new linked list's pointer
        dummy = ListNode(0)
        new_list = dummy
        current = head.next  # Start from the node after the initial 0

        while current:
            current_sum = 0

            # Sum up the values between zeros
            while current and current.val != 0:
                current_sum += current.val
                current = current.next

            # If we've summed some values, create a new node
            if current_sum != 0:
                new_list.next = ListNode(current_sum)
                new_list = new_list.next

            # Move to the next segment after the next zero
            if current:
                current = current.next

        return dummy.next