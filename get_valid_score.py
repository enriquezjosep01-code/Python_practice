# josef A Enriquez
# python 
# valid score  ____ practice 

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
result = get_valid_score()
print("Final result:", result)
