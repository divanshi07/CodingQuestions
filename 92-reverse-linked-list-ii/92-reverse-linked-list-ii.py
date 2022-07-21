# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left>right:
            return head 
        prev = None;
        curr=head 
        
        i=1
        while curr is not None and i<left:
            prev=curr
            curr=curr.next 
            i+=1
        start=curr
        end=None 
        while curr is not None and i<=right:
            nxt=curr.next 
            curr.next=end
            end=curr
            curr=nxt
            i+=1
        if start:
            start.next=curr
            if prev is None:
                head=end 
            else:
                prev.next=end 
        return head