book_list = []

def main():
    while (True):
        print("\nWelcome to Personal Library Manager 📚")
        print("-----------------------------------\n")
        print("So let's get started!!! 🌟")
                
        menu = input(""" 
            [1] - Add a book
            [2] - Remove a book
            [3] - Search for a book
            [4] - Display all books
            [5] - Display statistics (total books, percentage read)
            [6] - Exit \t Use number(0-6) to press the key
    """)
        
        if menu == '1':
            print("Please Enter the details to add a new book")
            book_title = input("Book Name/Title: ")
            book_author = input("Author: ")
            while True:
                try:
                    book_publication_year = int(input("Publication Year: "))
                    if len(str(book_publication_year)) != 4:
                        print("Please enter a valid 4-digit publication year.")
                    else:
                        break  
                except ValueError:
                    print("Invalid input! Please enter a numeric value for the publication year.")
            book_genre = input("Genre: ")
            read = input('Read Status(Y/N): ').strip()
            book_read_status = True if read.lower() == 'y' else False
            book_list.append({
                "Book Name": book_title,
                "Book Author": book_author,
                "Publication Year": book_publication_year,
                "Genre": book_genre,
                "Read Status": book_read_status
            })
            
        elif menu == '2':
            book_remove = input("Which book do you want to remove? (enter a book name) ")
            found = False
            for book in book_list:
                if book["Book Name"].lower() == book_remove.lower():
                    book_list.remove(book)
                    print(f"✅ Book '{book_remove}' removed.")
                    found = True
                    break  
            if not found:
                print(f"❌ Book '{book_remove}' not found.")
                    
        elif menu == '3':
            search_book = input("Enter a book(name): ")
            found = False
            for book in book_list:
                if book["Book Name"].lower() == search_book.lower():
                    print(book)
                    found = True
            if not found:
                print(f"❌ Book '{search_book}' not found.")
            
        elif menu == '4':
            if len(book_list) == 0:
                print("No Book Found")
            else:
                print("📚 Your Library:")
                for idx, book in enumerate(book_list, start=1):
                    print(f"\nBook {idx}")
                    for key, value in book.items():
                        print(f"  {key}: {value}")
                
        elif menu == '5':
            if len(book_list) == 0:
                print("No Books Found")
            else:
                print(f"The total number of books = {len(book_list)}")
                total_read = sum(1 for book in book_list if book["Read Status"] == True)
                read_percentage = (total_read / len(book_list)) * 100
                print(f"The total read percentage = {read_percentage:.2f}%")
        
        elif menu == '6':
            print("Exiting the library manager. Goodbye! 👋")
            break  


main()
