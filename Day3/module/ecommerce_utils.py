# You are asked to build a simple E-commerce Billing System using Python modules.
#     1. Create a module file named ecommerce_utils.py that contains the following functions:
#     -apply_discount(price, discount_percent) → applies a discount and returns the discounted price.
#     -add_gst(price, gst_percent=18) → adds GST (default 18%) and returns the new price.
#     -generate_invoice(cart, discount_percent=0, gst_percent=18) → accepts a dictionary cart (with product names as keys and prices as values) and prints a detailed invoice.
#     2. Create a main program file named main.py that:
#     Imports the ecommerce_utils module.
#     Creates a shopping cart (dictionary) with at least 3 products.
#     Calls the module functions to generate an invoice.
#     Expected Output Example:
#     ------ INVOICE ------
#     Laptop          : ₹55000
#     Phone           : ₹30000Headphones      : ₹2000
#     ---------------------
#     Subtotal: ₹87000
#     After 10% discount: ₹78300.0
#     After 18% GST: ₹92454.00
#     ---------------------
#     Thank you for shopping with us!

def apply_discount(price, discount_percent):
    """Apply a discount to the price and return the discounted price."""
    discount_amount = (discount_percent / 100) * price
    return price - discount_amount 

def add_gst(price, gst_percent=18):
    """Add GST to the price and return the new price."""
    gst_amount = (gst_percent / 100) * price
    return price + gst_amount  

def generate_invoice(cart, discount_percent=0, gst_percent=18):
    """Generate and print a detailed invoice."""
    print("------ INVOICE ------")
    subtotal = 0

    for product, price in cart.items():
        print(f"{product:<15}: ₹{price}")
        subtotal += price

    print("-" * 21)
    print(f"Subtotal: ₹{subtotal}")

    if discount_percent > 0:
        discounted_price = apply_discount(subtotal, discount_percent)
        print(f"After {discount_percent}% discount: ₹{discounted_price:.2f}")
    else:
        discounted_price = subtotal

    final_price = add_gst(discounted_price, gst_percent)
    print(f"After {gst_percent}% GST: ₹{final_price:.2f}")
    print("-" * 21)
    print("Thank you for shopping with us!")