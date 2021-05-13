class GradeBook:

    def __init__(self):
        self.grade_book = []
        self.name = None
        self.grade = 0


    def add_grade(self, grade):
        self.grade = grade
        self.grade_book.append(self.grade)
        

    def __iter__(self):
        yield from self.grade_book