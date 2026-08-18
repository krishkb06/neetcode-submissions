# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        #initialize list1 and 2 variables

        l1 = list1
        l2 = list2

        #initialize listnode for head of new list, remember that there will be a dummy 0 node attached to head
        head = ListNode()
        #set up an iterable current node pointing to head so that we do not affect the head and can return it
        curr = head

#while both lists still have values, build the new list
        while l1 and l2:
            #compare l1.val and l2.val, if l1.val is less than or equal then put that NODE into the list (curr.next), then move both curr and l1 foward
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                #same comparison idea just this time if l2 is bigger add l2 into the list
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
#now suppose that you reach a point where one list doesnt have values anymore, check that either l1 in this case or later l2 is empty and then while the other list still has values add in the nodes and iterate the list and curr
        if not l1:
            while l2:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        
        if not l2:
            while l1:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
#finally return head.next instead of head due to the dummy 0 that was added when you initialized the list node
        return head.next

            
        