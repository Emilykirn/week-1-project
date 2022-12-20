### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['j.k. rowling', 'c.s. lewis', 'victoria aveyard', 'brene brown']

# Now let's add a new author to the end with the .append() method. Type your code below.
my_authors.append('delia owens')
# Code here
# Example: my_authors.append("H.G. Wells")


# Now let's remove an element in the list
my_authors.remove('j.k. rowling')
# Code here
# Example: my_authors.remove("H.G. Wells")


# Now access an element by it's index. (Remember it indexes start at 0.)
my_authors[0]
# Code here
# Example: my_authors[2]


# Now slice the list.
my_authors[2:]
# Code here
# Example: my_authors[1:4]


### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.
authors_tuple_list = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson")
# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###
authors_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson"}
# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.
authors_set.add("Delia Owens")
# Code here
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.
authors_set.add("Delia Owens")
print(authors_set)
# Code here
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.


# Code here
for book in my_authors:
    print(book)

for book in authors_set:
    print(book)

for item in authors_tuple_list:
    print(item)

# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

