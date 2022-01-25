from data_loader import get_student_data



student_data = get_student_data()

class Student:
    def __init__(self, student_number, name, courses):
        self.student_number = student_number
        self.name = name
        self.courses = courses
        self.activities = []

    def get_name(self):
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_courses(self):
        return self.courses
    
def get_students():
    students_list = [] 

    for key in student_data:
        first_name = student_data[key][0]
        last_name = student_data[key][1]
        
        courses = []
        for i in range(2, 7):
            if (student_data[key][i]) != '':
                courses.append(student_data[key][i])

        students_list.append(Student(key, first_name +" " +last_name, courses))

    return students_list
