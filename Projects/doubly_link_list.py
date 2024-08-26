class node:
    def __init__(self,Val):
        self.data=Val
        self.next=None
        self.prev=None

def insert_at_head(head,val):
    n=node(val)
    n.next=head
    head.prev=n
    head=n
    return head
def insert_at_tail(head,val):
    n=node(val)
    if head is None:
        head=n
        return head
    
    temp=head
    while temp.next is not None:
        temp=temp.next
    
    temp.next=n
    n.prev=temp

def display(head):
    temp=head

    while temp!=None:
        print(temp.data)
        temp=temp.next

if __name__ == "__main__":
    head=None
    head=insert_at_tail(head,10)
    head=insert_at_head(head,5)
    display(head)
        