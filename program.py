import time
from grade_book import GradeBook


if __name__ == "__main__":
    
    grade_books = []
    
    print("Welcome to a Grade Book")
    
    while True:
        try:
            control_center = int(input("What would you like to do: \n1)Create Grade Book \n2)View Grade Books \n3)Add and view Grades\n4)Calculate average Grade\n5)Delete Grade Book\n6)Exit\n>"))
        except ValueError:
            print("Enter only numbers")
            continue    
        if control_center == 1:
            grade_book = GradeBook()
            grade_book.name = input("Name your Grade Book: ")
            grade_books.append(grade_book)
            print()
            print("Your added new Grade Book and it is named {}".format(grade_book.name))
            print()
            continue
        elif control_center == 2:
            if not grade_books:
                print()
                print("There are no Grade Books")
                print()
            counter = 1
            print()
            for grade_book in grade_books:
                print(f"Your Grade Book {counter} named: {grade_book.name}")
                counter +=1
            print()
        elif control_center == 3:
            if not grade_books:
                print()
                print("You must create Grade Book first")
                print()
                continue
            for grade_book in grade_books:
                print(grade_book.name)
            select_grade_book = input("Select Grade Book: ")
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
            action = input("Would You like to 'add' grades to this Grade Book or to 'view' it: ")
            if action.lower() == "add":
                while True:
                    try:
                        question = input("Enter Grade or enter 'done' to finish: ")
                        if question == "done":
                            break
                        elif question != "done":
                            grade = question 
                            selected_grade_book.add_grade(int(grade)) 
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
                print("You must create Grade Book first")
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
                print("Please type existed Grade Book")
        elif control_center == 5:
            if not grade_books:
                print()
                print("You must create Grade Book first")
                print()
                continue
            for grade_book in grade_books:
                print(grade_book.name)
            select_grade_book = input("Type Grade Book To Delete: ")
            for grade_book in grade_books:
                if select_grade_book == grade_book.name:
                    grade_books.remove(grade_book)    
                    print()
                    print(f"Grade Book named {grade_book.name} is deleted")
                    print()
                    break
        elif control_center == 6:
            print("Exiting")
            time.sleep(1)
            break
        