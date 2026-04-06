class Book :
  @classmethod
  def user_input(cls):
    cls.book_id=int(input("Enter book id : "))
    cls.author=input("Enter author name : ")
    cls.title=input("Enetr book name :")
    cls.isbn=int(input("Enter isbn number : "))
    cls.year=int(input("Enter year of publication : "))
    cls.genre=input("Enter genre of book : ")
    return cls(cls.book_id,cls.author,cls.title,cls.isbn,cls.year,cls.genre)
  def __init__(self,book_id,author,title,isbn,year,genre):
    self.book_id=book_id
    self.author=author
    self.title=title
    self.isbn=isbn
    self.year=year
    self.genre=genre

    self.is_borrowed=False
    self.borrower=None
    self.due_date=None
    self.borrow_count=0
  
  def is_available(self):
    if self.is_borrowed==False:
      return True
    else:
      return False
    
  def borrow(self,duedate,member_id):
    if self.is_available()==True:
      self.isborrowed=True
      self.borrower=member_id
      self.borrow_count=self.borrow_count+1
      self.duedate=duedate
      print("Book borrowed successfully!")
      return True
    else:
      print("Sorry, the book is currently unavailable.")
      return False
  def return_book(self):
    if self.isborrowed==True:
      self.isborrowed=False
      self.borrower=None
      self.duedate=None
      print("Book returned successfully!")
    else :
      print("This book is not currently borrowed.")
