consumption_unit = int(input("Enter the consumption unit "))
per_unit_price = 10


total_amount = consumption_unit * per_unit_price

gst = (total_amount * 5)/100

final_amount = total_amount + gst

print("Total amount is ", final_amount)