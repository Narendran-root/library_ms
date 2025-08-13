import books
import members
import transactions
import reports
import exports

def main_menu():
    while True:
        print("\n===== Library Management System =====")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Reports")
        print("6. Export Reports")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            books.list_books()
            print("a. Add Book | u. Update Book | d. Delete Book")
            sub = input("Enter choice: ")
            if sub == "a": books.add_book()
            elif sub == "u": books.update_book()
            elif sub == "d": books.delete_book()

        elif choice == "2":
            members.list_members()
            print("a. Add Member")
            sub = input("Enter choice: ")
            if sub == "a": members.add_member()

        elif choice == "3":
            transactions.borrow_book()

        elif choice == "4":
            transactions.return_book()

        elif choice == "5":
            reports.borrowed_books_with_members()
            reports.books_borrowed_by_category()

        elif choice == "6":
            exports.export_borrowed_books_csv()

        elif choice == "0":
            break

if __name__ == "__main__":
    main_menu()
