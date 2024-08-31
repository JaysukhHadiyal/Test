class StudentInformation:
    def set_information(self, name, age, student_Id):
        self.name = name
        self.age = age
        self.student_Id = student_Id
        print(f'name: {self.name}, age: {self.age}')


class StudentGrades(StudentInformation):
    def calculate_student_mark(self):
        student_mark = [int(mark) for mark in input("Enter grades separated by commas: ").replace(',', ' ').split()]
        return student_mark

    def Average(self):
        stud_marks = self.calculate_student_mark()
        if not stud_marks:
            print(f'Student_ID: {self.student_Id}')
        else:
            average = sum(stud_marks) / len(stud_marks)
            print(f'Student ID: {self.student_Id}, Average is: {average}')


while True:
    try:
        name = input("Enter student name: ")
        if not name.isalpha():
            raise ValueError("Pz Enter a name field .")
        age = int(input("Enter age: "))
        if age <= 0:
            raise ValueError("Age must be a positive integer.")
        student_Id = int(input("Enter Student Id "))
        if not student_Id:
            print("Plz Enter student Id in integer ")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

p1 = StudentGrades()
p1.set_information(name, age, student_Id)
p1.Average()