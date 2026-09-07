# Josef A Enriquez 
# python 
# class_average.py
def get_valid_student_count():
    while True:
        try:
            students = int(input("How many students there are in your classroom?."))
        except ValueError:
            print("thats not a number, try again")
            continue

        if students<=0:
            print("number shuuld be greater than 0. otherwise it will keep asking you to enter a greater number.")
            continue

        return students

student_average = 0
number_student = get_valid_student_count()
def score_number():
     while True:
        try:
            score = float(input("Enter student score."))
        except ValueError:
            print("that's not a number, try again!!")
            continue

        if score<0:
            print("it cannot be less than 0")
            continue

        return score

for y  in range (number_student):
    score = score_number()
    student_average=student_average + score
    
total_average = student_average / number_student

print(f"your average score is: {total_average:.2f}")