# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None:
            q = head.next
            head.next = None
            while q != None:
                temp = q.next
                q.next = head
                head = q
                q = temp
        return (head)