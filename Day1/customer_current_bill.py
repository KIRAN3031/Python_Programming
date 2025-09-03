c_number,c_name=map(str,input("Enter customer number and name: ").split())
c_present_bill,c_previous_bill=map(float,input("Enter present and previous bill: ").split())
c_total_units = c_present_bill - c_previous_bill
c_total_bill = c_total_units * 3.80
print("Customer Number: ",c_number)
print("Customer Name: ",c_name)
print("Total Units Consumed: ",c_total_units)
print("Total Bill: ",c_total_bill)