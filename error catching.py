class Error(Exception):
    pass

class valueTooBigError(Error):
    pass

class valueTooSmallError(Error):
    pass

subject_list = ["english language", "english literature", "maths", "chemistry", "physics", "biology", "computer science", "art", "geography", "spanish"]

grades_list = []


def gcseGrade():

    for i in subject_list:
        
        grade = int(input(f"Enter {i} grade (0 = U grade): "))
        if grade > 9:
            raise valueTooBigError
        elif grade < 0:
            raise valueTooSmallError
        if grade == 1:
            print("bad grade")
            grades_list.append(grade)
        elif grade == 2:
            print("bad grade")
            grades_list.append(grade)
        elif grade == 3:
            print("bad grade")
            grades_list.append(grade)
        elif grade == 4:
            print("bad grade")
            grades_list.append(grade)
        elif grade == 5:
            print("getting frisky, are we?")
            grades_list.append(grade)
        elif grade == 6:
            print("decent grade")
            grades_list.append(grade)
        elif grade == 7:
            print("good grade")
            grades_list.append(grade)
        elif grade == 8:
            print("good grade")
            grades_list.append(grade)
        elif grade == 9:
            print("good grade")
            grades_list.append(grade)

    average_grade = sum(grades_list) / len(grades_list)
    print(f"Average grade: {average_grade}")


enteredGrade = False

while enteredGrade is False:
    #global grade
    try:
        gcseGrade()
        enteredGrade = True
    except ValueError: 
        print("You entered the incorrect type, try the whole thing again")
    except valueTooBigError:
        print("You entered a grade higher than 9, please restart from the beginning")
    except valueTooSmallError:
        print("You entered a number smaller than 0, please restart from the beginning")