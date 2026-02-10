#https://leetcode.com/problems/merge-two-sorted-lists/
#Level: Easy
#Time Complexity: O(n + m), n = len(list1), m = len(list2)
#Space Complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = ListNode
        sortedListHead = sortedList


        while list1 != None and list2 != None:

            if list1.val <= list2.val:
                sortedList.next = list1
                list1 = list1.next
            else:
                sortedList.next = list2
                list2 = list2.next

            sortedList = sortedList.next

        if list1 == None:
            sortedList.next = list2
        if list2 == None:
            sortedList.next = list1
        
        return sortedListHead.next



        