string = input("Enter a string: ")

def total_words(string):
    words = string.split()
    print("Total number of words:", len(words))

total_words(string)
