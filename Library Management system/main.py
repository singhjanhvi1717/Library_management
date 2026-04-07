from book import Book
from member import Member
from library import Library

def main():
    my_library = Library()
    
    while True:
        # Menu display karo
        print("\n" + "="*40)
        print("    LIBRARY MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Display All Members")
        print("7. Exit")
        print("-"*40)
        
        choice = input("Enter your choice (1-7): ")
        
          
        if choice == "1":
            print("\n--- Add New Book ---")
            book = Book.user_input()
            my_library.add_book(book)
            print("Book added to library successfully!")
        
        elif choice == "2":
            print("\n--- Register New Member ---")
            member = Member.user_input()
            my_library.add_member(member)
            print("Member registered successfully!")
        
        elif choice == "3":
            print("\n--- Borrow Book ---")
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            my_library.borrow_books(book_id, member_id)
        
        elif choice == "4":
            print("\n--- Return Book ---")
            book_id = input("Enter Book ID: ")
            member_id = input("Enter Member ID: ")
            my_library.return_books(book_id, member_id)
        
        elif choice == "5":
            my_library.display_all_books()
        
        elif choice == "6":
            my_library.display_all_members()
        
        elif choice == "7":
            print("\nThank you for using Library Management System!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()
