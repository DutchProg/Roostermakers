import random
import math
import schedule
import data_loader as load
import courses
import visuals
import student
import string
import malus_calc
import pickle
import sys

def single_loop():
    student_data = student.get_students()
    student_data.pop(0)

    # we fetch our course data from the datafile
    course_data = load.get_data()

    # we initialize our week structure
    week_data = schedule.Week()

    course_activity = courses.get_courses()
    # we load all the activities into the courses and append the courses into a list
    courses_list = course_activity[0]

    # we make a new map to copy our activities in seperately, tis is a shallow copy so we do actually change the main location
    activity_list = course_activity[1]


    # we then iterate over all the activities and put it in the first availible slot
    # there are 145 slots total for 93 activities 



    #we loop trough the activities
    random.shuffle(activity_list)

    # alle activiteiten random in het rooster plakken op plekken waar de capaciteit klopt
    for activity in activity_list:
    
        smallest_room_count = 9999

        random.shuffle(week_data.day_list())

        for day in week_data.day_list():
            random.shuffle(day.timeslot_list())
            for timeslot in day.timeslot_list():
                random.shuffle(timeslot.room_list())
                for room in timeslot.room_list():
                    
                    if room.occupied() == False and activity.flag == False and room.max_capacity >= activity.capacity:
                        if room.max_capacity - activity.capacity < smallest_room_count:
                            if  room.night == False:
                                smallest_room_count = room.max_capacity - activity.capacity
                                smallest_room = room
                                day_small = day
                                timeslot_small = timeslot
                            if room.night == True:
                                
                                backup_room = room
                                day_small_backup = day
                                timeslot_small_backup = timeslot
                    
        smallest_room.add_activity(activity)
        if smallest_room_count != 9999:
            activity.set_activity(day_small,timeslot_small,smallest_room)
        else:
            print("hi")
            activity.set_activity(day_small_backup,timeslot_small_backup,backup_room)


    # per course checken welke studenten de course volgen en ze indelen in de activities, vervolgens de activities opslaan in de student class.
    for student_individual in student_data:

        for course in courses_list:
    
            if course.name in student_individual.courses:
                
                course.add_student(student_individual)

    return [ malus_calc.malus_calc(student_data,activity_list) , [student_data,courses_list,activity_list,week_data] ] 

malus =  9999 

for i in range(50000):
    loop = single_loop()
    solution = loop[1]
    malus_temp = loop[0] 

    if malus_temp < malus:
        malus = malus_temp
        solution_short = solution

sys.setrecursionlimit(3000)
print(malus)
config_dictionary = {"solution" : solution_short[3], "maluspunten" : malus}

with open(r"config.dictionary", "rb") as input_file:
    e = pickle.load(input_file)
    current_lowest = e["maluspunten"]




with open('config.dictionary', 'wb') as config_dictionary_file:
 
  # Step 3
    if config_dictionary["maluspunten"] < current_lowest: 
        pickle.dump(config_dictionary, config_dictionary_file)
    pickle.dump(e, config_dictionary_file)


visuals.plotter(solution_short[3])



with open("config.dictionary", "rb") as input_file:
    e = pickle.load(input_file)
    print(e)
    print(e["solution"])
    print(e["maluspunten"])