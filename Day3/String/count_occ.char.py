def count(s,char):
    return s.count(char)

string = input("Enter the string")
char = input("Enter the character to find the frequency")
print(f"The frequecy of {char} in {string} is ",count(string,char))