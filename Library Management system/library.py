from book import Book
from member import Member

class Library :
  def __init__(self):
    self.books={}
    self.members={}
  def add_book(self,book):
    self.books[book.book_id]=book
  def add_member(self,member):
    self.members[member.member_id]=member
  def borrow_books(self,book_id,member_id):
    if book_id in self.books and member_id in self.members:
      book=self.books[book_id]
      member=self.members[member_id]
      if book.is_available() and member.can_borrow():
        book.borrow(member_id)
        member.borrow_book(book_id)
        print(f"{member.name} borrowed {book.title}")
        return True
      else:
        print(f"{member.name} cannot borrow {book.title}")
        return False
  def return_books(self,book_id,member_id):
    if book_id in self.books and member_id in self.members:
      book=self.books[book_id]
      member=self.members[member_id]
      if book.borrower==member_id:
        book.return_book()
        member.return_book(book_id)
        print(f"{member.name} returned {book.title}")
        return True
      else:
        print(f"{member.name} cannot return {book.title}")
        return False

  def display_all_books(self):
    if not self.books:
        print("No books in library")
        return
    
    print("\n=== ALL BOOKS ===")
    for book_id, book in self.books.items():
        book.book_details()
        print("-" * 30)

  def display_all_members(self):
    if not self.members:
        print("No members registered")
        return
    
    print("\n=== ALL MEMBERS ===")
    for member_id, member in self.members.items():
        member.display_member_info()
        print("-" * 30)
      
