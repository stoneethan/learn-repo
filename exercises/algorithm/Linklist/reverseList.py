from utils.linked_list import *

class Solution:
    def rverseList(self,head):
        prev=None
        current=head

        while current:
            next_node=current.next
            current.next=prev
            prev=current
