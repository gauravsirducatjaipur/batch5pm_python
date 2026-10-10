# A shopkeeper sell three type of item ItemA, ItemB, ItemC. The price of ItemA is 100, ItemB is 80, ItemC is 200. Write a python program to calculate the total amount of items purchased by the customer.
qtyA =int(input("How many item do u want to purchase of type A: "))
qtyB =int(input("How many item do u want to purchase of type B: "))
qtyC =int(input("How many item do u want to purchase of type C: "))

total_amount = (qtyA * 100) + (qtyB * 80) + (qtyC * 200)
print("Your total amount is: ", total_amount)

gst = total_amount * 0.05
final_amount = total_amount + gst

print("Your final amount with GST is: ", final_amount)

# A coinbox contain different type of coin like 5rs, 2rs, 1rs, 50paisa, 25 paisa. Write a python program to calculate the total amount in terms of rs and paisa.

qty_5 = int(input("How many coin of rs 5 do u want to enter : "))
qty_2 = int(input("How many coin of rs 2 do u want to enter : "))
qty_1 = int(input("How many coin of rs 1 do u want to enter : "))
qty_50 = int(input("How many coin of paisa 50 do u want to enter : "))
qty_25 = int(input("How many coin of paisa 25 do u want to enter : "))

total_amount = (qty_5 * 500) + (qty_2 * 200) + (qty_1 * 100) + (qty_50 * 50) + (qty_25 * 25) 
print("Your total amount in terms of paisa is: ",total_amount)

# rs = int(total_amount/100)
rs = total_amount//100
paisa = total_amount % 100
print("Total rs. = ", rs)
print("Total paisa = ", paisa)
