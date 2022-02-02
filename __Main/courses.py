import math
import data_loader
import student 

course_data = data_loader.get_data()

class Activity:
    def __init__(self, name, type, capacity, id):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.flag = False
        self.day = ""
        self.time = ""
        self.room = ""
        self.students = []
        self.id = name+"-" + str(id)

    def __repr__(self):
        rep = "{} {}".format(self.id, self.type)
        return rep


    def set_activity(self, day, time, room):
        self.flag = True
        self.day = day
        self.time = time
        self.room = room

    def add_student(self,student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        else:
            return False

    def remove_student(self,student):
        
        
        self.students.remove(student)

        return True






class Course:
    def __init__(self, name, E_students, number_of_lectures, number_of_tutorials, capacity_tutorial, number_of_practica, capacity_practica):
        self.name = name
        self.E_students = E_students
        self.number_of_lectures = number_of_lectures
        self.number_of_tutorials = number_of_tutorials
        self.number_of_practica = number_of_practica
        self.capacity_tutorial = capacity_tutorial
        self.capacity_practica = capacity_practica
        self.activity_list = []

        if capacity_practica != 0:
            self.absolute_nr_practica = math.ceil(E_students/capacity_practica)*number_of_practica
        else:
            self.absolute_nr_practica= 0
        if capacity_tutorial != 0:
            self.absolute_nr_tutorial = math.ceil(E_students/capacity_tutorial)*number_of_tutorials
        else:
            self.absolute_nr_tutorial=0
        self.total_number_of_activities = number_of_lectures+ self.absolute_nr_practica  + self.absolute_nr_tutorial
        
        for i in range(int(self.number_of_lectures)):
            self.activity_list.append(Activity(name, "lecture", E_students, 1 ))

        for i in range(int(self.absolute_nr_practica)):
            self.activity_list.append(Activity(name, "practica", capacity_practica, i ))

        for i in range(int(self.absolute_nr_tutorial)):
            self.activity_list.append(Activity(name, "tutorial",capacity_tutorial,i ))

    def get_name(self):
        return self.name

    def get_E_students(self):
        return self.E_students

    def get_number_of_lectures(self):
        return self.number_of_lectures

    def get_number_of_tutorials(self):
        return self.number_of_tutorials

    def get_number_of_practica(self):
        return self.number_of_practica

    def get_total_activities(self):
        return self.total_number_of_activities

    def get_activity_list(self):
        return self.activity_list
    
    def add_student(self,student):

        count_practical = 0
        count_tutorial = 0
        count_lecture = 0

        for activity in self.activity_list:
            present = False
            for student_2 in activity.students:
                if student.name == student_2.name:
                    present = True
            if activity.type == "lecture" and count_lecture< self.number_of_lectures and present == False:
                if activity.add_student(student) == True:
                    student.add_activity(activity)
                    count_lecture += 1
            if activity.type == "practica" and count_practical < self.number_of_practica and  present == False:
                if activity.add_student(student) == True:
                    student.add_activity(activity)
                    count_practical +=1 
            if activity.type == "tutorial" and count_tutorial < self.number_of_tutorials and  present == False:
                if activity.add_student(student) == True:
                    student.add_activity(activity)
                    count_tutorial +=1 
    
        


        #Naam - 0#Hoorcolleges,#Werkcolleges,Max. stud.,#Practica,Max. stud.,E(studenten)
        # we have a dict with name of course as key, and number of students lecture_count, tutorial_count, tut_max and practica_count and prac,maxin a list
        #name, E_students, number_of_lectures, number_of_tutorials, number_of_practica, capacity_tutorial, capacity_practica)
student_data = student.get_students()

def get_courses():
    courses_list = [] 
    for key in course_data:
        student_count = 0
        for student in student_data:
            for course in student.courses:
                if course == key:
                    student_count +=1

        courses_list.append(Course(key, student_count, course_data[key][1], course_data[key][2], course_data[key][3], course_data[key][4], course_data[key][5]))

    activity_data = []
    for i in courses_list:
        for k in i.get_activity_list():

            activity_data.append(k)

    return [courses_list, activity_data]


