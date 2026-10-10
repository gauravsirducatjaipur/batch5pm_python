library_fee = 3500

delay_days = int(input("Enter the delay days of submission amount "))
per_day_fine = 75

final_fees = library_fee + (delay_days * per_day_fine)

print("The final fees is ", final_fees)
