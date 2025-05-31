# List of available books
books = ["The Lion King", "Frozen", "Cinderella"]
print("Pick one of the books: The Lion King, Frozen, Cinderella")
# Function to display available books
def show_books():
    print("\n📗📘 Books in the library:")
    for book in books:
        print("- " + book)

# Function to borrow a book
def borrow_book():
    name = input("Enter the name of the book to borrow: ")
    if name in books:
        books.remove(name)
        print(f"✅ You borrowed: {name}")
    else:
        print("❌ Book not available")

# Function to return a book
def return_book():
    name = input("Enter the name of the book to be returned: ")
    books.append(name)
    print(f"🔁 You have returned a book titled: {name}")

# Menu 
while True:
    print("\nWhat do you want to do?")
    print("1. View all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == '1':
        show_books()
    elif choice == '2':
        borrow_book()
    elif choice == '3':
        return_book()
    elif choice == '4':
        break
    else:
        print("❌ Invalid choice")
