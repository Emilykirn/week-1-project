
my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}
book_list = [ 
{  
    "title": "Reminders of Him",
    "author": "Colleen HOover",
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
# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(book_dictionary):
    info_on_book = f'Title: {book_dictionary["title"]}. \nAuthor: {book_dictionary["author"]} \nWritten in the year: {book_dictionary["year"]}\nRating: {book_dictionary["rating"]} \nPages: {book_dictionary["pages"]}'

    return (info_on_book)

print(book_parser(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def display_book_title(book_dictionary):
    book_title = book_dictionary["title"]
    return book_title

def display_book_author(book_dictionary):
    book_author = book_dictionary["author"]
    return book_author

def display_book_year(book_dictionary):
    book_year = book_dictionary["year"]
    return book_year

def display_book_rating(book_dictionary):
    book_rating = book_dictionary["rating"]
    return book_rating

def display_book_pages(book_dictionary):
    book_pages = book_dictionary["pages"]
    return book_pages

print(display_book_title(my_book))
print(display_book_author(my_book))
print(display_book_year(my_book))
print(display_book_rating(my_book))
print(display_book_year(my_book))

# or 
def from_dict_to_str(book_dictionary):
    return f"book: {book_dictionary['title']}\n Author: {book_dictionary['author']}"

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

#return highest rated book:

# def highest_rated_book(book_dictionary_list):
    # current_max_rating = 0
    # for book_dictionary in book_dictionary_list:
    #     if book_dictionary["ratings"] >= current_max_rating

    # print(current_max_rating)
    # return(current_max_rating)

def get_total_pages(book_dictionary_list):
    total_pages = 0

    for book_dictionary in book_dictionary_list:
        total_pages += book_dictionary["pages"]

    return total_pages

def get_title(book_dictionary_list):
    return book_dictionary_list.get("title", "no title")

def get_authors(book_dictionary_list):
    return book_dictionary_list.get("author", "no author")
