# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        #gcd = ListNode()
        def recursive_gcd(a,b):
            if b==0:
                return a
            else:
                return recursive_gcd(b, a%b)

        while curr and curr.next:
            gcd = ListNode()
            gcd.val = recursive_gcd(curr.val,curr.next.val)
            
            gcd.next= curr.next
            curr.next = gcd
            curr  = gcd.next

        return head


            


        

