#josef A 
# python 
#grade_calculator

# ask the user to enter numeric test score.
grade = int(input("Enter your score."))

if grade < 0 or grade > 100:
    print("your score is not valid - Enter a new score between 0 and 100.")
    grade = int(input("what was your score?."))


if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade >=60:
    print("D")
elif grade <60:
    print("F")
else:
    print(F"your final score was {grade} congratulations.")