#josef A 
# python 
#grade_calculator

def get_valid_score():
    while True:
        try:
             score = int(input("Enter your score:"))
        except  ValueError:
            print("that's not a number. Try again.")
            continue

        if score <0 or score>100:
            print("NOt valid.  Insert a number between 0 and 100.")
            continue

        return score # it hands over the value to get_valid_code.
#    its just dead code result = get_valid_score()print("Final result:", result)

grade = get_valid_score()
if grade>=90:# was using a while loop, it keeps printing forever
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
elif grade <=60:
    print("F")
# death code else:
# print(F"your final score was {grade} you fail.")

if grade>=60:
    print(f"congratulations. your final grade was {grade} you have passed.")
else:
    print(f"your score was {grade} lower than 60, you have failed!")