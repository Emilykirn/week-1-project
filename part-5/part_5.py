### Step 1 - Store data in a .txt


## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def menu(book_source):
    active = True

    while active:
    
        choice = input("Select 1 to add a book.\n Select 2 to see authors.\n Select 3 to view books")

        if choice == "1":
            book_source.append(my_new_book())
        elif choice =="2":
            print(print_all_authors(book_source))
        elif choice =="3":
            print(view_books())
        else:
            print("Choose options 1 or 2")

menu()


def my_new_book():

    with open('library.txt', 'a') as file:
        file.write(f'{title}, {author}, {year}, {rating}, {pages}\n')
    title = str(input("What is the title of the book you would like to add? - "))
    author = str(input("Who is the author of the book you would like to add? - "))
    try: 
        year = int(input("In what year was this book published? - "))
    except:
        year = int(input("Please type a number for the year? - "))
    try:
        rating = float(input("What rating would you give this book? - "))
    except:
        rating = float(input("Plese type a number for the rating? - "))
    try:
        pages = int(input("How many pages are in this book? - "))
    except:
        pages = int(input("Please type a number for number of pages? - "))


def print_all_authors(list_of_authors):

    print("\nHere are the authors...\n")

    for book in list_of_authors:
        author = book["author"]
        
        print(f"Author: {author}")
        

def view_books(book_source):

    print("\nHere are all your books...\n")
    
    with open(book_source, "r") as f:
        file = f.readlines()
        
        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_dictionary = {
            'title': str(title),
            "author": str(author),
            "year": int(year),
            "rating": float(rating),
            "pages": int(pages)
        }

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

view_books()

if __name__ == "__main__":
    menu()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here




### Step 3 - 


## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script



### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!




# with open("books.txt", "w") as book_file:
#     book_file.write(the_hobbit.__str__())

