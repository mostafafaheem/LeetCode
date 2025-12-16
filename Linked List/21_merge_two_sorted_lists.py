# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        retlist = None
        temp1 = None
        temp2 = None
        tmpret = None
        while list1 and list2:
            if list1.val >= list2.val:
                temp2 = list2.next
                if retlist:
                    retlist.next = list2
                    retlist = retlist.next
                else:
                    retlist = list2
                    tmpret = retlist
                list2 = temp2
            elif list2.val > list1.val:
                temp1 = list1.next
                if retlist:
                    retlist.next = list1
                    retlist = retlist.next
                else:
                    retlist = list1
                    tmpret = retlist
                list1 = temp1
        if list1:
            retlist.next = list1
        elif list2:
            retlist.next = list2
        return tmpret
