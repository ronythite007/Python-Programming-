class linked_node:

    def __init__(self,x):
        self.data=x
        self.next=None

    def display_node(self):
        return self.data
    
    def next_node(self):
        return self.next
    
class linked_list:

    def __init__(self):
        self.head=None

    def inserting(self,data):

        #checking list empty
        
        if self.head is None:
            self.head=linked_node(data)
        
        else:
            temp =self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=linked_node(data)
    
    def insert_at_head(self,data):
        new=linked_node(data)
        new.next=self.head
        self.head=new
    
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "-->", end=" ")
            temp = temp.next
    

obj=linked_list()

obj.inserting(1)
obj.inserting(2)
obj.inserting(3)
obj. insert_at_head(10)
obj.display()