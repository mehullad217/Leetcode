# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        slow = fast = dummy
        while fast and fast.next:
            fast =fast.next.next
            slow=slow.next

    
        if fast:
            return slow.next
        else:
            return slow

        