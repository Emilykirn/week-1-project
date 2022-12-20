### Step 1 - Input function
# fave_book = input('What is your favorite book? ') 

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.
# Code here
# def my_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     year = int(input("In what year was this book published? - "))
#     rating = float(input("What rating would you give this book? - "))
#     pages = int(input("How many pages are in this book? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     return book_dictionary


# my_new_book()



### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def my_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     year = int(input("In what year was this book published? - "))
#     rating = float(input("What rating would you give this book? - "))
#     pages = int(input("How many pages are in this book? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.
from operator import truediv


book_list = [ 
{  
    "title": "Reminders of Him",
    "author": "Colleen Hoover",
    "year": 2022,
    "rating": 4.1,
    "pages": 335
},
{
    "title": "Art of War",
    "author": "Sun Tzu",
    "year": 496,
    "rating": 4.6,
    "pages": 232
},
{  
    "title": "Where The Crawdads Sing",
    "author": "Delia Owens",
    "year": 2018,
    "rating": 4.8,
    "pages": 400
},
{  
    "title": "The Last Thing He Told Me",
    "author": "Laura Dave",
    "year": 2021,
    "rating": 4.3,
    "pages": 316
}
]
# Code here
def my_new_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
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

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return book_dictionary


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def print_all_authors(list_of_authors):

    print("\nHere are the authors...\n")

    for book in list_of_authors:
        author = book["author"]
        
        print(f"Author: {author}")

def menu(book_source):
    active = True

    while active:
    
        choice = input("Choose 1 to add a book.\n Choose 2 to see authors")

        if choice == "1":
            book_source.append(my_new_book())
        elif choice =="2":
             print_all_authors(book_source)
        else:
            print("Choose options 1 or 2")

menu(book_list)


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here



