# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """Given the head of a singly linked list, reverse the list, and return the reversed list.

        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr:
            next_head = curr.next
            curr.next = prev
            prev = curr
            curr = next_head
        return prev
