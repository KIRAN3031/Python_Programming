def check_char_dig_spl(ch):
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        return 'Character'
    elif ch.isdigit():
        return 'Digit'
    else:
        return "Special Character"
ch = input("Enter the character")
print(f'the character the user entered is a {check_char_dig_spl(ch)}')