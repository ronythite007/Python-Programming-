class library:
    def __init__(self):
        
        self.nobook=0
        self.book=[]

    def adding_book(self,books):
        self.book.append(books)
        self.nobook=len(self.book)

    def show_no_of_book(self):
        print(f"The books are {self.book}")
        print(f"The no. of books are {self.nobook}")
    
rohan=library()
b=int(input("enter how many book to add : "))
for i in range(1,b):
    a=input(f"Enter the book {i} : ")
    rohan.adding_book(a)
rohan.show_no_of_book()