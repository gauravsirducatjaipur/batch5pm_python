hindi = float(input("Enter the marks od hindi subject "))
english = float(input("Enter the marks od english subject "))
maths = float(input("Enter the marks od maths subject "))
science = float(input("Enter the marks od science subject "))
social = float(input("Enter the marks od social subject "))

total = hindi + english + maths + science + social 

percentage = (total / 5)
print("your percentage is ", percentage, "\t\t\ttotal is", total)