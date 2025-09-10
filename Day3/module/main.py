#     Create a main program file named main.py that:
#     Imports the ecommerce_utils module.
#     Creates a shopping cart (dictionary) with at least 3 products.
#     Calls the module functions to generate an invoice.
import ecommerce_utils as e
# E-commerce Billing System
cart = {
    "Laptop": 55000,
    "Phone": 30000,
    "Headphones": 2000
}
e.generate_invoice(cart, discount_percent=10, gst_percent=18)
print()