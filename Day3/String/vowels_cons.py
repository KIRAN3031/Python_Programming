string = input("Enter a string: ")

def count_v_c(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print("Total vowels:", vowel_count)
    print("Total consonants:", consonant_count)

count_v_c(string)
