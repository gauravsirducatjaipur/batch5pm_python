# 15 Python Nested If Practice Questions

These questions are based on real-life scenarios. Students must use nested `if` statements to solve each problem.

## 1. Electricity Bill Calculation

Write a Python program to input the number of electricity units consumed and calculate the electricity bill according to the following rates.

| Units consumed | Rate per unit |
| -------------- | ------------- |
| 1–100          | ₹5            |
| 101–200        | ₹7            |
| 201–300        | ₹10           |
| Above 300      | ₹12           |

Conditions:

- If units are less than or equal to 0, display `"Invalid units"`.
- Calculate the bill using the applicable rate for all units consumed.

Example: If consumption is 150 units, the bill is calculated using the first 100 units at ₹5 and the remaining 50 units at ₹7.

## 2. Employee Bonus Calculation

Write a Python program to input an employee's gender, years of experience, and monthly salary. Calculate the bonus according to the following conditions.

| Gender | Experience        | Bonus         |
| ------ | ----------------- | ------------- |
| Male   | 10 years or more  | 15% of salary |
| Male   | 5–9 years         | 10% of salary |
| Male   | Less than 5 years | 5% of salary  |
| Female | 10 years or more  | 20% of salary |
| Female | 5–9 years         | 12% of salary |
| Female | Less than 5 years | 7% of salary  |

Conditions:

- First check whether the gender is Male or Female.
- Inside that condition, check the years of experience.
- Display the bonus amount and the total salary after adding the bonus.
- Reject invalid salary or experience values.

## 3. Student Grade Calculation

Write a Python program to input marks in three subjects: Python, SQL, and Web Development.

Calculate the total, percentage, and grade according to these conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90–100     | A+    |
| 80–89.99   | A     |
| 70–79.99   | B     |
| 60–69.99   | C     |
| 40–59.99   | D     |
| Below 40   | Fail  |

Conditions:

- Each subject must have marks between 0 and 100.
- First check whether the student has passed all three subjects (minimum 33 marks in each).
- If the student passes all subjects, calculate the grade based on percentage.
- Otherwise, display `"Fail"`.

## 4. Income Tax Calculation

Write a Python program to input a person's annual income and calculate tax based on the following slabs.

| Annual income        | Tax rate |
| -------------------- | -------- |
| Up to ₹3,00,000      | 0%       |
| ₹3,00,001–₹6,00,000  | 5%       |
| ₹6,00,001–₹9,00,000  | 10%      |
| ₹9,00,001–₹12,00,000 | 15%      |
| Above ₹12,00,000     | 20%      |

Conditions:

- First validate the annual income.
- Use nested `if` statements to identify the applicable slab.
- For this exercise, apply the selected rate to the entire income.
- Display the tax amount and income after tax.

Note: This is a programming exercise with simplified tax rules, not an actual tax calculation.

## 5. Shopping Discount Calculator

Write a Python program to input the total shopping amount and customer type.

| Customer type  | Purchase amount | Discount |
| -------------- | --------------- | -------- |
| Regular        | ₹1,000 or more  | 5%       |
| Regular        | ₹5,000 or more  | 10%      |
| Premium        | ₹1,000 or more  | 10%      |
| Premium        | ₹5,000 or more  | 20%      |
| Any valid type | Below ₹1,000    | 0%       |

Conditions:

- First check whether the customer is Regular or Premium.
- Then check the purchase amount using nested `if` statements.
- Display the discount and final payable amount.
- Reject negative purchase amounts and invalid customer types.

## 6. Loan Eligibility Checker

Write a Python program to determine whether a person is eligible for a loan.

| Condition       | Requirement     |
| --------------- | --------------- |
| Age             | 21–60 years     |
| Monthly salary  | ₹25,000 or more |
| Work experience | 2 years or more |
| Credit score    | 700 or more     |

Conditions:

- First check the person's age.
- If the age is eligible, check monthly salary.
- Then check work experience.
- Finally, check the credit score.
- Display the reason for rejection or `"Eligible for loan"`.

## 7. Employee Salary Increment

Write a Python program to calculate an employee's salary increment based on performance rating and years of experience.

| Performance rating | Experience           | Increment |
| ------------------ | -------------------- | --------- |
| Excellent          | 5 years or more      | 20%       |
| Excellent          | Below 5 years        | 15%       |
| Good               | 5 years or more      | 12%       |
| Good               | Below 5 years        | 8%        |
| Average            | Any valid experience | 5%        |
| Poor               | Any valid experience | 0%        |

Conditions:

- Input employee name, current salary, experience, and performance rating.
- First check the performance rating.
- Inside each rating condition, check experience where required.
- Display the increment amount and revised salary.

## 8. ATM Withdrawal System

Write a Python program to simulate an ATM withdrawal.

Conditions:

- Input the account balance, withdrawal amount, and PIN.
- First check whether the PIN is correct (use `1234` as the correct PIN).
- If the PIN is correct, check whether the withdrawal amount is positive.
- If the amount is valid, check whether sufficient balance is available.
- The withdrawal amount must be a multiple of ₹100.
- Display the appropriate message and the remaining balance.

## 9. Insurance Premium Calculator

Write a Python program to calculate an insurance premium based on age, gender, and smoking status.

| Age   | Gender           | Smoker | Annual premium |
| ----- | ---------------- | ------ | -------------- |
| 18–30 | Male             | Yes    | ₹12,000        |
| 18–30 | Male             | No     | ₹8,000         |
| 18–30 | Female           | Yes    | ₹10,000        |
| 18–30 | Female           | No     | ₹7,000         |
| 31–50 | Male             | Yes    | ₹20,000        |
| 31–50 | Male             | No     | ₹14,000        |
| 31–50 | Female           | Yes    | ₹16,000        |
| 31–50 | Female           | No     | ₹11,000        |
| 51–65 | Any valid gender | Any    | ₹25,000        |

Conditions:

- First check age eligibility (18–65).
- Then check gender.
- For ages 18–50, check smoking status.
- For ages 51–65, use the fixed premium.
- Display the applicable premium.

This is a hypothetical classroom pricing model, not real insurance advice or a recommended pricing policy.

## 10. Restaurant Bill Calculator

Write a Python program to calculate a restaurant bill based on the order amount and membership type.

| Membership           | Bill amount    | Discount |
| -------------------- | -------------- | -------- |
| Regular              | ₹2,000 or more | 5%       |
| Gold                 | ₹2,000 or more | 10%      |
| Platinum             | ₹2,000 or more | 15%      |
| Any valid membership | Below ₹2,000   | 0%       |

Conditions:

- Input customer name, bill amount, and membership type.
- First check the membership type.
- Then check the bill amount.
- Add 5% GST after applying the discount.
- Display the original bill, discount, GST, and final bill.

## 11. Mobile Data Plan Selection

Write a Python program to calculate a mobile recharge price based on the selected plan and customer type.

| Plan     | Validity | Price |
| -------- | -------- | ----- |
| Basic    | 28 days  | ₹199  |
| Standard | 56 days  | ₹399  |
| Premium  | 84 days  | ₹599  |

Conditions:

- Input the plan name and customer type (Regular or Student).
- First validate the plan.
- If the plan is valid, check the customer type.
- Students receive a 10% discount on any plan.
- Display the final recharge amount and validity.

## 12. Vehicle Insurance Eligibility

Write a Python program to calculate a hypothetical vehicle insurance premium based on vehicle type and vehicle age.

| Vehicle type | Vehicle age   | Premium |
| ------------ | ------------- | ------- |
| Bike         | 0–3 years     | ₹2,000  |
| Bike         | Above 3 years | ₹3,000  |
| Car          | 0–3 years     | ₹5,000  |
| Car          | Above 3 years | ₹8,000  |
| Truck        | 0–3 years     | ₹10,000 |
| Truck        | Above 3 years | ₹15,000 |

Conditions:

- First check the vehicle type.
- Then check the vehicle age.
- Reject negative vehicle ages and unsupported vehicle types.
- Display the applicable premium.

## 13. Employee Attendance and Salary Deduction

Write a Python program to calculate an employee's salary after attendance-based deductions.

Assume a monthly salary of ₹30,000 and 30 working days.

| Attendance | Deduction |
| ---------- | --------- |
| 26–30 days | 0%        |
| 21–25 days | 5%        |
| 16–20 days | 10%       |
| 0–15 days  | 20%       |

Conditions:

- Input the number of days attended.
- First validate that attendance is between 0 and 30.
- Use nested `if` statements to determine the deduction.
- Display the deduction amount and final salary.

## 14. Hospital Consultation Fee

Write a Python program to calculate a consultation fee based on patient age and appointment type.

| Patient age | Appointment type | Fee    |
| ----------- | ---------------- | ------ |
| Below 12    | General          | ₹300   |
| Below 12    | Specialist       | ₹600   |
| 12–59       | General          | ₹500   |
| 12–59       | Specialist       | ₹1,000 |
| 60 or above | General          | ₹400   |
| 60 or above | Specialist       | ₹800   |

Conditions:

- Input patient age and appointment type.
- First check the patient's age group.
- Inside each age group, check the appointment type.
- Reject negative ages and invalid appointment types.
- Display the consultation fee.

## 15. Online Exam Eligibility

Write a Python program to determine whether a student can appear in an online examination.

| Condition        | Requirement           |
| ---------------- | --------------------- |
| Attendance       | 75% or more           |
| Assignment score | 40 or more out of 100 |
| Fees             | Paid                  |
| Registration     | Completed             |

Conditions:

- Input attendance percentage, assignment score, fee status, and registration status.
- First check attendance.
- If attendance is sufficient, check the assignment score.
- If the score is sufficient, check fee payment.
- Finally, check registration.
- Display the exact reason if the student is not eligible.

## Bonus Challenge: Nested If Practice

For every question, students should follow this approach:

1. Take input from the user.
2. Validate the input.
3. Use nested `if` statements.
4. Perform the calculation where required.
5. Display the final result.

Important: These questions are designed for practicing nested `if` statements, not just `if-elif-else`. Encourage students to put one `if` statement inside another `if` block wherever the problem's conditions require it.