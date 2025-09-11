class payment:
    def pay(self, amount):
        pass

# create subclasses card_payment, cash_payment, upi_payment that overides the pay method
class card_payment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using card")


class cash_payment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using cash")


class upi_payment(payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# create a list of payment objects (cash_payment, card_payment, upi_payment)

payments = [cash_payment(), card_payment(), upi_payment()]
amount = 1000
for p in payments:
    p.pay(amount)