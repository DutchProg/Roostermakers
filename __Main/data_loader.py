import csv

def get_data():
    course_data = {}
    
    with open('Courses.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for element in list(reader):

            #Naam #Hoorcolleges,#Werkcolleges,#Max.stud,#Practica,#Max.stud,#E(studenten)
            if int(element[2]) == 0:
                if int(element[4]) == 0:
                    course_data[element[0]] = [int(element[-1]), int(element[1]), int(element[2]), 0, int(element[4]), 0]
                else:
                    course_data[element[0]] = [int(element[-1]), int(element[1]), int(element[2]), 0, int(element[4]), int(element[5])]
            elif int(element[4]) == 0:
                if int(element[2]) == 0:
                    course_data[element[0]] = [int(element[-1]), int(element[1]), int(element[2]), 0, int(element[4]), 0]
                else:
                    course_data[element[0]] = [int(element[-1]), int(element[1]), int(element[2]), int(element[3]), int(element[4]), 0]
            else:
                course_data[element[0]] = [int(element[-1]), int(element[1]), int(element[2]), int(element[3]), int(element[4]), int(element[5])]
    return course_data


def get_student_data():
    student_data = {}
    
    with open('studentenenvakken.csv',  encoding='latin1') as f:
        reader = csv.reader(f)

        for row in reader:

            student_data[row[2]] = [row[1], row[0], row[3], row[4], row[5], row[6], row[7]]

    return student_data

