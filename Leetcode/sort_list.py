# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """Given the head of a linked list, return the list after sorting it in ascending order.
        
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
        curr = head
        lst = sorted(lst)
        for i in lst:
            curr.val = i
            curr = curr.next
        return head
