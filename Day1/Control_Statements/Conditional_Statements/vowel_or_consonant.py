def vowel_or_consonant(ch):
    l = ['a','e','i','o','u','A','E','I','O','U']
    if ch in l:
        print("Vowel")
    else:
        print("Consonant")

ch = input("Enter a character: ")
vowel_or_consonant(ch)
