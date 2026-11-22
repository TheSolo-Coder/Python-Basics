# If Statement

age = 20

if age >= 18:
    print("You are an adult.")


# If and Else

score = 35

if score >= 50:
    print("You passed!")
else:
    print("You failed.")


# If, Elif and Else

score = 85

if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Grade C")


# Multiple Independent If Statements

temperature = 30

if temperature > 20:
    print("It is warm.")

if temperature > 25:
    print("It is hot.")


# Nested If Statements

age = 20
has_permission = True

if age >= 18:
    if has_permission:
        print("Access granted!")


# Conditions with User Input

age = int(input("Enter Your Age: "))

if age >= 18:
    print("Entry allowed!")
else:
    print("Entry not allowed.")


# Final Challenge: Grading System

score = int(input("Enter Your Score: "))

if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Grade F")
