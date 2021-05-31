import time
from grade_book import GradeBook


if __name__ == "__main__":
    
    grade_books = []
    
    print("Welcome to a GradeBook")
    
    while True:
        try:
            control_center = int(input("What would you like to do: \n1)Create GradeBook \n2)View GradeBooks \n3)Add and view Grades\n4)Calculate average Grade\n5)Delete GradeBook\n6)Exit\n>"))
        except ValueError:
            print("Enter only numbers")
            continue    
        if control_center == 1:
            grade_book = GradeBook()
            grade_book.name = input("Name your GradeBook: ")
            grade_books.append(grade_book)
            print()
            print("Your added new GradeBook and it is named {}".format(grade_book.name))
            print()
            continue
        elif control_center == 2:
            if not grade_books:
                print()
                print("There are no GradeBooks")
                print()
            counter = 1
            print()
            for grade_book in grade_books:
                print(f"Your GradeBook {counter} named: {grade_book.name}")
                counter +=1
            print()
        elif control_center == 3:
            if not grade_books:
                print()
                print("You must create GradeBook first")
                print()
                continue
            for grade_book in grade_books:
                print(grade_book.name)
            select_grade_book = input("Select GradeBook: ")
            for grade_book in grade_books:
                if select_grade_book == grade_book.name:
                    selected_grade_book = grade_book
                    print(f"Grade Book selected {selected_grade_book.name}")
                    break
            if select_grade_book != grade_book.name:
                print()
                print("Name must be equal")
                print()
                continue    
            action = input("Would You like to 'add' grades to this GradeBook or to 'view' it: ")
            if action.lower() == "add":
                while True:
                    try:
                        question = input("Enter Grade or enter 'done' to finish: ")
                        if question == "done":
                            break
                        elif question != "done":
                            grade = int(question)
                            if grade <= 0 or grade > 5:
                                print("Grade must be greater than 0 and or equal to 5")
                                continue
                            else:
                                selected_grade_book.add_grade(grade) 
                                continue
                    except ValueError:
                        print("Value must be 'number' or 'done'")
                        continue
            elif action.lower() == "view":
                for grade in selected_grade_book:
                    print(grade)
                    time.sleep(0.5)
        elif control_center == 4:
            if not grade_books:
                print()
                print("You must create GradeBook first")
                print()
                continue
            for grade_book in grade_books:
                print(grade_book.name)
            select_grade_book = input("Type Grade Book To Calculate Average Grade: ")
            for grade_book in grade_books:
                if select_grade_book == grade_book.name:
                    selected_grade_book = grade_book
                    if len(selected_grade_book.grade_book) == 0:
                        print()
                        print("You must enter grades first")
                        print()
                        continue
                    else:
                        total = 0
                        length = 0
                        for grade in selected_grade_book:
                            total += grade
                            length += 1 
                        print()           
                        print("Average grade is {}".format(total / length))
                        print()
                        break                  
            else:
                print("Please type existed GradeBook")
        elif control_center == 5:
            if not grade_books:
                print()
                print("You must create GradeBook first")
                print()
                continue
            for grade_book in grade_books:
                print(grade_book.name)
            select_grade_book = input("Type Grade Book To Delete: ")
            for grade_book in grade_books:
                if select_grade_book == grade_book.name:
                    grade_books.remove(grade_book)    
                    print()
                    print(f"GradeBook named {grade_book.name} is deleted")
                    print()
                    break
        elif control_center == 6:
            print("Exiting")
            time.sleep(1)
            break
        