# CONDITIONS (15PTS TOTAL)
from math import sqrt

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.
grade = int(float(input('Give me a percentage grade: ')))
if grade > 100:
    print("Error, that's not a grade.")
elif 97 <= grade <= 100:
    print("A+")
elif 93 <= grade <= 96:
    print("A")
elif 90 <= grade <= 92:
    print("A-")
elif 87 <= grade <= 89:
    print("B+")
elif 83 <= grade <= 86:
    print("B")
elif 80 <= grade <= 82:
    print("B-")
elif 77 <= grade <= 79:
    print("C+")
elif 73 <= grade <= 76:
    print("C")
elif 70 <= grade <= 72:
    print("C-")
elif 67 <= grade <= 69:
    print("D+")
elif 65 <= grade <= 66:
    print("D")
elif 0 <= grade <= 64:
    print("F")
elif grade < 0:
    print("Error, that's not a grade.")

# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many
'''different'''  # vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.
string = input("Supply a string: ").lower()
vowels = 0
for i in ['a', 'e', 'i', 'o', 'u']:
    if i in string:
        vowels += 1
if vowels == 1:
    print("There is a vowel in the string.")
elif vowels:
    print("There are", vowels, "different vowels in the string.")
else:
    print("There aren't any vowels in the string.")
# PROBLEM 3 (Quadratic Equation - 6pts)
print('''I can solve quadratic equations using the quadratic formula.
Quadratic equations are of the form Ax^2 + Bx + C = 0.''')
A = float(input("A= "))
B = float(input("B= "))
C = float(input("C= "))
# Such equations have zero, one or two solutions.

# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.
if not A or not B:
    print("A, B have to be nonzero.")
    quit()
if B ** 2 - 4 * A * C < 0:
    print("There are no solutions.")
    quit()
first_solution = (-1 * B + sqrt(B ** 2 - 4 * A * C)) / (2 * A)
second_solution = (-1 * B - sqrt(B ** 2 - 4 * A * C)) / (2 * A)
if B ** 2 - 4 * A * C == 0:
    print("x =", first_solution)
else:
    print("x1 =", first_solution)
    print("x2 =", second_solution)
