def check_aplhabet_or_not(a):
    if a.isalpha():
        print("It is an alphabet")
    else:
        print("It is not an alphabet")

a = input("Enter a character: ")
check_aplhabet_or_not(a)