# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k==0:
            return head

        n=1
        last = head

        while last.next:

            n+=1

            last=last.next 

        k = k%n

        if k == 0:

            return head

        t = head

        for _ in range(1,n-k):

            t=t.next

        last.next = head

        new_head = t.next

        t.next = None

        return new_head
        