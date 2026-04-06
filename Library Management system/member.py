from book import Book

class Member :
  @classmethod
  def user_input(cls):
    member_id=input("Enter member id :")
    name=input("Enter member name:")
    email_id=input("Enter email id :")
    phone_number=int(input("Enter phone number :"))
    return cls(member_id ,name,email_id,phone_number)
  def __init__ (self,member_id,name,email_id,phone_number):
    self.member_id=member_id
    self.name=name
    self.email_id=email_id
    self.phone_number=phone_number
    self.borrowed_books=[]
    self.borrow_history=[]
    self.total_borrowed=0

  def can_borrow(self):
      if len(self.borrowed_books)<3:
        print("Member can borrow more books.")
        return True
      else:
        print("Member has reached the borrowing limit.")
        return False
  def borrow_book(self,book_id):
      if self.can_borrow()==True:
        self.borrowed_books.append(book_id)
        self.borrow_history.append(book_id)
        self.total_borrowed=self.total_borrowed+1
        print("Book borrowed successfully!")
        return True
      else:
        print("Cannot borrow more books.")
        return False 
  def return_book(self,book_id):
      if book_id in self.borrowed_books:
        self.borrowed_books.remove(book_id)
        print("Book returned successfully!")
      else:
        print("This book is not currently borrowed by the member.")
    
  def display_member_info(self):
      print("Member Id :",self.member_id)
      print("Member NAme : ",self.name)
      print("Email Id : ",self.email_id)
      print("Phone Number : ",self.phone_number)
      print("Borrowed Books : ",self.borrowed_books)
      print("List of total borrowed books : ",self.borrow_history)
      print("Total number of books borrowed : ",self.total_borrowed)