class ECommerceCart:
    def __init__(self, cart_items=None):
        if cart_items is None:
            self.cart_items = []
        else:
            self.cart_items = cart_items

    def add(self, item):
        if item not in self.cart_items:
            self.cart_items.append(item)
        else:
            print("Item already in cart.")

    def remove(self, item):
        if item in self.cart_items:
            self.cart_items.remove(item)
        else:
            print("Item not found in cart.")

    def search(self, item):
        return item in self.cart_items

    def display(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("Cart items:", ', '.join(str(i) for i in self.cart_items))

    def total_products(self):
        print(f"The number of products in the cart are: {len(self.cart_items)}")
        print(f'They are :',self.cart_items)

    def sort(self):
        self.cart_items.sort()
        print("The sorted cart is ",self.cart_items)
    
    def clear(self):
        self.cart_items.clear()
        print("The cart is cleared",self.cart_items)


print('Enter the input for the cart')
cart = ECommerceCart()

while True:
    print("\nMenu:")
    print("1. Add element")
    print("2. Remove element")
    print("3. Search element")
    print("4. Display elements")
    print("5. Show the total number of products in the cart")
    print("6. Sort the cart ")
    print('7. Clear the cart')
    print("8. Exit")

    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        item = input("Enter the item to add: ")
        cart.add(item)
    elif choice == '2':
        item = input("Enter the item to remove: ")
        cart.remove(item)
    elif choice == '3':
        item = input("Enter the item to search: ")
        if cart.search(item):
            print(f"{item} is in the cart.")
        else:
            print(f"{item} is not in the cart.")
    elif choice == '4':
        cart.display()
    elif choice == '5':
        cart.total_products()
    elif choice=='6':
        cart.sort()
    elif choice=='7':
        cart.clear()
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
