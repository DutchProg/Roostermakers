import csv



def get_data():
    course_data = {}
    with open('Courses.csv') as f:
        reader = csv.reader(f)
        next(reader)
        for element in list(reader):
            #Naam - 0#Hoorcolleges,#Werkcolleges,Max. stud.,#Practica,Max. stud.,E(studenten)
            # we have a dict with name of course as key, and number of students lecture_count, tutorial_count, tut_max and practica_count and prac,maxin a list
            if int(element[2])== 0:
                if int(element[4]) == 0:
                    course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),0,int(element[4]),0]
                else:
                    course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),0,int(element[4]),int(element[5])]
            elif int(element[4]) == 0:
                if int(element[2])== 0:
                    course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),0,int(element[4]),0]
                else:
                    course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),int(element[3]),int(element[4]),0]
            else:
                course_data[element[0]] = [int(element[-1]),int(element[1]),int(element[2]),int(element[3]),int(element[4]),int(element[5])]
    return course_data
            