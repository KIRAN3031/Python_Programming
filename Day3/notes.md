================================================
------------------Day 3 ------------------------
================================================


# DATA STRUCTURES
    1. Sequence
    2. Sets
    3. Dictionary
--------------------------------------------------

# Sequence
    1. list
    2. tuple
    3. string
----------------------------------------------------

# list
    list slicing
    1. ordered
    2. mutable
    3. duplicates allowed
    4. heterogenous data
    ## method
        1. adding elements -> .append(), .insert()
        2. removing -> .remove(), .pop() ,.del
        3. searching -> .index()
        4. sorting -> .sort()
        5. built-ins -> len(),min(),max(),sum()
------------------------------------------------------

## problems
    1. demonstrate list
    2. negative numbers in list
    3. second largest number in the list
    4. even and odd count of the given list
    5. delete the element without using the in-built methods
    6. count the frequency of each and every element in the list
    7. print the unique elements in the list
    8. count the number of duplicate elements in the list
    9. delete the duplicate elements in the list and print the unique elements 
    10. ecommerce application in python.
        using the following operations using lists:
            1. Add a product to the cart
            2. remove a product ot the cart
            3. Search for a product in the cart
            4. Display all products in the cart
            5. show the total number of products in the cart
 
--------------------------------------------------------------------------------------------

# tuple
    tuple slicing
    1. ordered
    2. immutable
    3. duplicates are allowed
    4. heterogenous data types
    5. parentheses

## problems
    1. store the data of 5 students in a list of tuples.
    2. print the name fo the students who scored the highest marks
    3. print all studnets who scored more than 75 marks

# String
    1. len of the string
    2. concatenate the strings
    3. program to countthe total number of characters, digits and special characters in the string
    4. program to count the total number of vowels and consonants in a string
    5. write a program to count total number of words in a string
    6. Write a program to search all occurrences of a character in given string
    7. write a program to count occurrences of a charcter in given string
    8. write a program to get the output as follows:
        input : aaabbca
        output : a4b2c1
    9. write a program to find highest frequency character in a string
    10. write a program to find lowest frequecy charcter in a string

# Sets
    1. No Duplicates
    2. unordered
    3. mutable
    4. heterogenous
    5. unindexed

## Set Operations:
    1. Union (∪)

        Symbol: |
        Method: union()
        Description: Returns a new set with all elements from both sets.
    
    2. Intersection (∩)

        Symbol: &
        Method: intersection()
        Description: Returns a new set with elements common to both sets.

    3. Difference (−)

        Symbol: -
        Method: difference()
        Description: Returns a new set with elements in the first set but not in the second.

    4. Symmetric Difference (elements in either set, but not both)

        Symbol: ^
        Method: symmetric_difference()
        Description: Returns a new set with elements in either the first or second set but not in both.

## set Methods
    add(elem): Add an element to the set.

    remove(elem): Remove an element; raises KeyError if not found.

    discard(elem): Remove an element if present; no error if absent.

    clear(): Remove all elements from the set.

    pop(): Remove and return an arbitrary element.

    update(*others): Update the set with the union of itself and others.


### problems
    A 3-day tech workshop collected attendee registrations separately for each day. You are given three lists (day1, day2, day3) of email addresses — lists may contain duplicates (people registering multiple times) and email case may vary (Upper/Lower).
        1. Write a Python program that:
        2. Cleans each day's list (normalizes case, removes duplicates).
        3. Prints the total number of unique attendees across all days.
        4. Prints the list of attendees who attended all three days.
        5. Prints the list of attendees who attended exactly one day.
        6. Prints pairwise overlap counts (day1 & day2, day2 & day3, day1 & day3).
        7. Produces a final report with counts and sorted lists for each of the above outputs.

# Dictonary
    Key-value pairs — Data stored as pairs with unique keys and associated values.

    Ordered (Python 3.7+) — Items maintain insertion order.

    Mutable — Keys and values can be added, updated, or removed.

    Keys must be immutable — e.g., strings, numbers, or tuples; lists or other dictionaries cannot be keys.

    Keys are unique — Duplicate keys are overwritten; only one value per key.

    Values can be heterogeneous and mutable — Values can be of any data type, including lists or other dictionaries.

    Keys are case-sensitive — 'Key' and 'key' are different.

## methods
    get(key, default=None) — Returns value for key or default if key not found.

    keys() — Returns a view of all keys.

    values() — Returns a view of all values.

    items() — Returns a view of (key, value) tuples.

    pop(key, default) — Removes key and returns its value; returns default if key not found.

    popitem() — Removes and returns the last inserted (key, value) pair.

    clear() — Removes all items.

    update(other_dict) — Adds or updates key-value pairs from another dictionary.

    copy() — Returns a shallow copy of the dictionary.

    setdefault(key, default) — Returns the value of key; if not found, inserts key with default value and returns default.

### problem

    You are building a Library Management System in Python. The system should store books in a dictionary where:
        . Key → Book ID
        . Value → Book Title
        Write a Python program to perform the following operations using Dictionaries:
        1. Add a book to the library (Book ID, Title).
        2. Remove a book using Book ID.
        3. Search for a book by Book ID and display the title.
        4. Update the title of a book (e.g., correction in title).
        5. Display all books in the library.
        6. Count the total number of books in the library.
        7. Check if a book title exists in the library (reverse lookup).

# Modules
    A module is a distinct, self-contained unit of code that groups related functions, classes, variables, or statements, typically saved in a file (e.g., with a .py extension in Python). It can be imported and reused in other programs to perform specific tasks.

    Code reusability
    Maintainability
    Organized code
    Collabration

## Types
    User defined
    Built in modules 
    External modules (Third party modules)

### problem
    You are asked to build a simple E-commerce Billing System using Python modules.
    1. Create a module file named ecommerce_utils.py that contains the following functions:
    -apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
    -add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
    -generate_invoice(cart, discount_percent=0, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
    2. Create a main program file named main.py that:
    Imports the ecommerce_utils module.
    Creates a shopping cart (dictionary) with at least 3 products.
    Calls the module functions to generate an invoice.
    Expected Output Example:
    ------ INVOICE ------
    Laptop          : ₹55000
    Phone           : ₹30000Headphones      : ₹2000
    ---------------------
    Subtotal: ₹87000
    After 10% discount: ₹78300.0
    After 18% GST: ₹92454.00
    ---------------------
    Thank you for shopping