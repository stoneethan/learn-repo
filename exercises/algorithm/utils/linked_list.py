class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def create_Link_List(values):
    dummy=ListNode()
    current=dummy

    for value in values:
        current.next=ListNode(value)
        current=current.next

    return dummy.next

def linked_list_to_list(head):
    result=[]

    while head:
        result.append(head.val)
        head=head.next

    return result

def print_linked_list(head):
    values=linked_list_to_list(head)
    print("->".join(map(str,values)))

    