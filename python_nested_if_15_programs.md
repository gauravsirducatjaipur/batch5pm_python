# Python Nested If – 15 Practice Programs

> Each program uses nested `if` statements. Save each program in a separate `.py` file and run it with Python.

---

## 1. Electricity Bill Calculation

```python
units = float(input("Enter electricity units consumed: "))

if units <= 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 5
    else:
        if units <= 200:
            bill = (100 * 5) + ((units - 100) * 7)
        else:
            if units <= 300:
                bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
            else:
                bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

    print(f"Electricity bill: ₹{bill:.2f}")
```

## 2. Employee Bonus Calculation

```python
gender = input("Enter gender (Male/Female): ").strip().lower()
experience = float(input("Enter years of experience: "))
salary = float(input("Enter monthly salary: "))

if salary <= 0 or experience < 0:
    print("Invalid salary or experience")
else:
    if gender == "male":
        if experience >= 10:
            bonus_rate = 15
        else:
            if experience >= 5:
                bonus_rate = 10
            else:
                bonus_rate = 5
    else:
        if gender == "female":
            if experience >= 10:
                bonus_rate = 20
            else:
                if experience >= 5:
                    bonus_rate = 12
                else:
                    bonus_rate = 7
        else:
            bonus_rate = 0
            print("Invalid gender")

    if gender == "male" or gender == "female":
        bonus = salary * bonus_rate / 100
        print(f"Bonus: ₹{bonus:.2f}")
        print(f"Salary after bonus: ₹{salary + bonus:.2f}")
```

## 3. Student Grade Calculation

```python
python_marks = float(input("Enter Python marks (0-100): "))
sql_marks = float(input("Enter SQL marks (0-100): "))
web_marks = float(input("Enter Web Development marks (0-100): "))

if not (0 <= python_marks <= 100 and 0 <= sql_marks <= 100 and 0 <= web_marks <= 100):
    print("Invalid marks")
else:
    total = python_marks + sql_marks + web_marks
    percentage = total / 3

    if python_marks < 33 or sql_marks < 33 or web_marks < 33:
        print("Fail")
    else:
        if percentage >= 90:
            grade = "A+"
        else:
            if percentage >= 80:
                grade = "A"
            else:
                if percentage >= 70:
                    grade = "B"
                else:
                    if percentage >= 60:
                        grade = "C"
                    else:
                        if percentage >= 40:
                            grade = "D"
                        else:
                            grade = "Fail"

        print(f"Total: {total:.2f}/300")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
```

## 4. Simplified Income Tax Calculation

For practice only: this exercise applies the selected rate to the **entire income**, not progressively by slab. It is not an actual tax calculation.

```python
income = float(input("Enter annual income (₹): "))

if income < 0:
    print("Invalid income")
else:
    if income <= 300000:
        tax_rate = 0
    else:
        if income <= 600000:
            tax_rate = 5
        else:
            if income <= 900000:
                tax_rate = 10
            else:
                if income <= 1200000:
                    tax_rate = 15
                else:
                    tax_rate = 20

    tax = income * tax_rate / 100
    print(f"Tax rate: {tax_rate}%")
    print(f"Tax amount: ₹{tax:.2f}")
    print(f"Income after tax: ₹{income - tax:.2f}")
```

## 5. Shopping Discount Calculator

```python
customer_type = input("Enter customer type (Regular/Premium): ").strip().lower()
amount = float(input("Enter shopping amount (₹): "))

if amount < 0:
    print("Invalid shopping amount")
else:
    if customer_type == "regular":
        if amount >= 5000:
            discount_rate = 10
        else:
            if amount >= 1000:
                discount_rate = 5
            else:
                discount_rate = 0
    else:
        if customer_type == "premium":
            if amount >= 5000:
                discount_rate = 20
            else:
                if amount >= 1000:
                    discount_rate = 10
                else:
                    discount_rate = 0
        else:
            discount_rate = -1
            print("Invalid customer type")

    if discount_rate >= 0:
        discount = amount * discount_rate / 100
        final_amount = amount - discount
        print(f"Discount: ₹{discount:.2f}")
        print(f"Final amount: ₹{final_amount:.2f}")
```

## 6. Loan Eligibility Checker

```python
age = int(input("Enter age: "))
salary = float(input("Enter monthly salary (₹): "))
experience = float(input("Enter work experience in years: "))
credit_score = int(input("Enter credit score: "))

if age < 0 or salary < 0 or experience < 0 or credit_score < 0:
    print("Invalid input")
else:
    if age < 21 or age > 60:
        print("Not eligible: age must be between 21 and 60")
    else:
        if salary < 25000:
            print("Not eligible: monthly salary must be at least ₹25,000")
        else:
            if experience < 2:
                print("Not eligible: at least 2 years of work experience required")
            else:
                if credit_score < 700:
                    print("Not eligible: credit score must be at least 700")
                else:
                    print("Eligible for loan")
```

## 7. Employee Salary Increment

```python
name = input("Enter employee name: ")
salary = float(input("Enter current monthly salary (₹): "))
experience = float(input("Enter years of experience: "))
rating = input("Enter performance rating (Excellent/Good/Average/Poor): ").strip().lower()

if salary <= 0 or experience < 0:
    print("Invalid salary or experience")
else:
    if rating == "excellent":
        if experience >= 5:
            rate = 20
        else:
            rate = 15
    else:
        if rating == "good":
            if experience >= 5:
                rate = 12
            else:
                rate = 8
        else:
            if rating == "average":
                rate = 5
            else:
                if rating == "poor":
                    rate = 0
                else:
                    rate = -1
                    print("Invalid performance rating")

    if rate >= 0:
        increment = salary * rate / 100
        print(f"Employee: {name}")
        print(f"Increment: ₹{increment:.2f}")
        print(f"Revised salary: ₹{salary + increment:.2f}")
```

## 8. ATM Withdrawal System

```python
correct_pin = "1234"
balance = float(input("Enter account balance (₹): "))
pin = input("Enter ATM PIN: ")

if balance < 0:
    print("Invalid account balance")
else:
    if pin == correct_pin:
        amount = float(input("Enter withdrawal amount (₹): "))

        if amount <= 0:
            print("Invalid withdrawal amount")
        else:
            if amount % 100 != 0:
                print("Withdrawal amount must be a multiple of ₹100")
            else:
                if amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= amount
                    print("Withdrawal successful")
                    print(f"Remaining balance: ₹{balance:.2f}")
    else:
        print("Incorrect PIN")
```

## 9. Insurance Premium Calculator

This is a hypothetical classroom pricing example, not real insurance advice.

```python
age = int(input("Enter age: "))
gender = input("Enter gender (Male/Female): ").strip().lower()
smoker = input("Do you smoke? (Yes/No): ").strip().lower()

if age < 18 or age > 65:
    print("Age must be between 18 and 65")
else:
    if age >= 51:
        premium = 25000
    else:
        if gender == "male":
            if smoker == "yes":
                if age <= 30:
                    premium = 12000
                else:
                    premium = 20000
            else:
                if smoker == "no":
                    if age <= 30:
                        premium = 8000
                    else:
                        premium = 14000
                else:
                    premium = -1
        else:
            if gender == "female":
                if smoker == "yes":
                    if age <= 30:
                        premium = 10000
                    else:
                        premium = 16000
                else:
                    if smoker == "no":
                        if age <= 30:
                            premium = 7000
                        else:
                            premium = 11000
                    else:
                        premium = -1
            else:
                premium = -1

    if premium >= 0:
        print(f"Annual premium: ₹{premium:.2f}")
    else:
        print("Invalid gender or smoking status")
```

## 10. Restaurant Bill Calculator

For this exercise, GST is calculated at 5% **after** applying the discount.

```python
customer_name = input("Enter customer name: ")
membership = input("Enter membership (Regular/Gold/Platinum): ").strip().lower()
bill = float(input("Enter bill amount (₹): "))

if bill < 0:
    print("Invalid bill amount")
else:
    if membership == "regular":
        if bill >= 2000:
            discount_rate = 5
        else:
            discount_rate = 0
    else:
        if membership == "gold":
            if bill >= 2000:
                discount_rate = 10
            else:
                discount_rate = 0
        else:
            if membership == "platinum":
                if bill >= 2000:
                    discount_rate = 15
                else:
                    discount_rate = 0
            else:
                discount_rate = -1
                print("Invalid membership")

    if discount_rate >= 0:
        discount = bill * discount_rate / 100
        discounted_bill = bill - discount
        gst = discounted_bill * 5 / 100
        final_bill = discounted_bill + gst

        print(f"Customer: {customer_name}")
        print(f"Original bill: ₹{bill:.2f}")
        print(f"Discount: ₹{discount:.2f}")
        print(f"GST (5%): ₹{gst:.2f}")
        print(f"Final bill: ₹{final_bill:.2f}")
```

## 11. Mobile Data Plan Selection

```python
plan = input("Enter plan (Basic/Standard/Premium): ").strip().lower()
customer_type = input("Enter customer type (Regular/Student): ").strip().lower()

if plan == "basic":
    price = 199
    validity = 28
else:
    if plan == "standard":
        price = 399
        validity = 56
    else:
        if plan == "premium":
            price = 599
            validity = 84
        else:
            price = -1
            validity = 0

if price < 0:
    print("Invalid plan")
else:
    if customer_type == "student":
        final_price = price - (price * 10 / 100)
    else:
        if customer_type == "regular":
            final_price = price
        else:
            final_price = -1

    if final_price < 0:
        print("Invalid customer type")
    else:
        print(f"Plan: {plan.title()}")
        print(f"Validity: {validity} days")
        print(f"Recharge amount: ₹{final_price:.2f}")
```

## 12. Vehicle Insurance Premium

This is a hypothetical classroom pricing example.

```python
vehicle_type = input("Enter vehicle type (Bike/Car/Truck): ").strip().lower()
vehicle_age = float(input("Enter vehicle age in years: "))

if vehicle_age < 0:
    print("Invalid vehicle age")
else:
    if vehicle_type == "bike":
        if vehicle_age <= 3:
            premium = 2000
        else:
            premium = 3000
    else:
        if vehicle_type == "car":
            if vehicle_age <= 3:
                premium = 5000
            else:
                premium = 8000
        else:
            if vehicle_type == "truck":
                if vehicle_age <= 3:
                    premium = 10000
                else:
                    premium = 15000
            else:
                premium = -1

    if premium >= 0:
        print(f"Insurance premium: ₹{premium:.2f}")
    else:
        print("Invalid vehicle type")
```

## 13. Attendance-Based Salary Deduction

```python
salary = 30000
working_days = 30
attendance = int(input("Enter days attended (0-30): "))

if attendance < 0 or attendance > working_days:
    print("Invalid attendance")
else:
    if attendance >= 26:
        deduction_rate = 0
    else:
        if attendance >= 21:
            deduction_rate = 5
        else:
            if attendance >= 16:
                deduction_rate = 10
            else:
                deduction_rate = 20

    deduction = salary * deduction_rate / 100
    final_salary = salary - deduction

    print(f"Monthly salary: ₹{salary:.2f}")
    print(f"Deduction rate: {deduction_rate}%")
    print(f"Deduction amount: ₹{deduction:.2f}")
    print(f"Final salary: ₹{final_salary:.2f}")
```

## 14. Hospital Consultation Fee

This is a hypothetical classroom fee schedule.

```python
age = int(input("Enter patient age: "))
appointment = input("Enter appointment type (General/Specialist): ").strip().lower()

if age < 0:
    print("Invalid age")
else:
    if appointment != "general" and appointment != "specialist":
        print("Invalid appointment type")
    else:
        if age < 12:
            if appointment == "general":
                fee = 300
            else:
                fee = 600
        else:
            if age <= 59:
                if appointment == "general":
                    fee = 500
                else:
                    fee = 1000
            else:
                if appointment == "general":
                    fee = 400
                else:
                    fee = 800

        print(f"Consultation fee: ₹{fee:.2f}")
```

## 15. Online Exam Eligibility

```python
attendance = float(input("Enter attendance percentage: "))
assignment_score = float(input("Enter assignment score (0-100): "))
fees_paid = input("Have fees been paid? (Yes/No): ").strip().lower()
registered = input("Is registration completed? (Yes/No): ").strip().lower()

if attendance < 0 or attendance > 100 or assignment_score < 0 or assignment_score > 100:
    print("Invalid attendance or assignment score")
else:
    if attendance < 75:
        print("Not eligible: attendance must be at least 75%")
    else:
        if assignment_score < 40:
            print("Not eligible: assignment score must be at least 40")
        else:
            if fees_paid != "yes":
                if fees_paid == "no":
                    print("Not eligible: fees have not been paid")
                else:
                    print("Invalid fee status")
            else:
                if registered == "yes":
                    print("Eligible for online examination")
                else:
                    if registered == "no":
                        print("Not eligible: registration is incomplete")
                    else:
                        print("Invalid registration status")
```
