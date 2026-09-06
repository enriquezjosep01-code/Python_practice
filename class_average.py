# Josef A Enriquez 
# python 
# class_average.py

students = int(input("How many students there are in your classroom?."))

while students<=0:
    print("Invalid - Enter a number greater than 0.")
    students = int(input("Enter how many students there are in your class?."))

score_average = 0

for y  in range(students):
    score = float(input("Enter student score."))
    score_average=score_average + score

total_average = score_average / students

print(f"your average score is: {total_average:.2f}")