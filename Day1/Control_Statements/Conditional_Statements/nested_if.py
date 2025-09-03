def marks(num):
    if num>=90:
        print("Grade A")
        if num>=95:
            print("Excellent")
        else:
            print("Good")
    elif num>=80:
        print("Grade B")
    else:
        print("Grade C")

marks(98)