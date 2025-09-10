string = input("Enter a string: ")
def count_dig_alph_spl(string):
    alphabets = 0
    digits = 0
    special_chars = 0

    for char in string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_chars += 1

    print("Total alphabets:", alphabets)
    print("Total digits:", digits)
    print("Total special characters:", special_chars)

count_dig_alph_spl(string)
