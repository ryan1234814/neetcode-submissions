# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        early,current=None,head
        while current :
            temp=current.next
            current.next=early
            early=current
            current=temp
        return early


        