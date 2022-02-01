import random
import math

import schedule
import data_loader as load
import courses
import visuals
import student
import malus_calc
import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np

def single_loop():
    student_data = student.get_students()
    student_data.pop(0)

    # we initialize our week structure
    week_data = schedule.Week()

    course_activity = courses.get_courses()
    # we load all the activities into the courses and append the courses into a list
    courses_list = course_activity[0]

    # we make a new map to copy our activities in seperately, tis is a shallow copy so we do actually change the main location
    activity_list = course_activity[1]


    #we loop trough the activities
    random.shuffle(activity_list)

    # alle activiteiten random in het rooster plakken op plekken waar de capaciteit klopt
    for activity in activity_list:
    
        smallest_room_count = 9999
        
        
        for day in sorted(week_data.day_list(),key=lambda _: random.random()):
            
            for timeslot in sorted(day.timeslot_list(),key=lambda _: random.random()):
                
                for room in sorted(timeslot.room_list(),key=lambda _: random.random()):
                    
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
            
            activity.set_activity(day_small_backup,timeslot_small_backup,backup_room)

    # per course checken welke studenten de course volgen en ze indelen in de activities, vervolgens de activities opslaan in de student class.
    for student_individual in student_data:

        for course in courses_list:
    
            if course.name in student_individual.courses:
                
                course.add_student(student_individual)

    return [student_data,courses_list,activity_list,week_data]

def course_switch_emptyslot(iterations_of_activitylist, solution ):

    student_data = solution[0]
    course_list =  solution[1]
    activity_list = solution[2]
    week_data = solution[3]
    changed_activity = 0
    malus_list = []

    for i in range(iterations_of_activitylist):

        for activity in activity_list:

            maluscount = malus_calc.malus_calc(student_data,activity_list)
            current_room = activity.room
            current_timeslot = activity.time
            current_day = activity.day
            changed = False

            for day in sorted(week_data.day_list(),key=lambda _: random.random()):
                
                for timeslot in sorted(day.timeslot_list(),key=lambda _: random.random()):
                    
                    for room in sorted(timeslot.room_list(),key=lambda _: random.random()):
                        
                        if room.occupied() == False and room.max_capacity >= activity.capacity and changed == False:

                            current_room.remove_activity()
                            room.add_activity(activity)
                            activity.set_activity(day,timeslot,room)
                            changed = True
                            malus_list.append(maluscount)  
                            changed_activity += 1
                            print(malus_calc.malus_calc(student_data,activity_list), maluscount)
                            
                            if malus_calc.malus_calc(student_data,activity_list) > maluscount:
                                changed = False
                                changed_activity -= 1
                                malus_list.pop()
                                room.remove_activity()
                                current_room.add_activity(activity)
                                activity.set_activity(current_day,current_timeslot,current_room)
    
    return changed_activity,malus_list,student_data,activity_list,week_data,course_list

def course_switch(iterations_of_activitylist, solution):
    student_data = solution[0]
    course_list =  solution[1]
    activity_list = solution[2]
    week_data = solution[3]
    changed_activity = 0
    malus_list = []

    for i in range(iterations_of_activitylist):

        for activity_1 in activity_list:
            
            maluscount = malus_calc.malus_calc(student_data,activity_list)
            current_room = activity_1.room
            current_timeslot = activity_1.time
            current_day = activity_1.day
            changed = False

            for day in sorted(week_data.day_list(),key=lambda _: random.random()):
                
                for timeslot in sorted(day.timeslot_list(),key=lambda _: random.random()):
                    
                    for room in sorted(timeslot.room_list(),key=lambda _: random.random()):
                        
                        if room.occupied() == True and room.max_capacity >= activity_1.capacity and changed == False:
                            

                            activity_2 = room.scheduled_activity[0]

                            current_room.remove_activity()
                            room.add_activity(activity_1)
                            current_room.add_activity(activity_2)

                            activity_1.set_activity(day,timeslot,room)

                            activity_2.set_activity(current_day,current_timeslot,current_room)

                            changed = True



                            malus_list.append(maluscount)  
                            changed_activity += 1
                            print(malus_calc.malus_calc(student_data,activity_list), maluscount)
                            
                            if malus_calc.malus_calc(student_data,activity_list) > maluscount:
                                changed = False
                                changed_activity -= 1
                                malus_list.pop()

                                room.remove_activity()
                                current_room.remove_activity()
                                room.add_activity(activity_2)
                                current_room.add_activity(activity_1)
                                activity_1.set_activity(current_day,current_timeslot,current_room)
                                activity_2.set_activity(day,timeslot,room)
    
    return changed_activity,malus_list,student_data,activity_list,week_data,course_list

def student_switch(iterations_of_activitylist, solution):
    student_data = solution[0]
    course_list =  solution[1]
    activity_list = solution[2]
    week_data = solution[3]
    
    changed_student = 0
    malus_list = []
    

    for i in range(iterations_of_activitylist):
        
        for student in student_data:
            maluscount = malus_calc.malus_calc(student_data,activity_list)
        
            for activity in student.activities:
                
                for activity_new in activity_list:

                    if activity.name == activity_new.name and activity.type == activity_new.type and student not in activity_new.students:
                        
                        if len(activity_new.students) != 0:
                            random_student = random.choice(activity_new.students)
                            
                        
                            activity.remove_student(student)
                            student.remove_activity(activity)
                            
                            
                            activity_new.remove_student(random_student)
                            random_student.remove_activity(activity_new)

                            activity.add_student(random_student)
                            student.add_activity(activity_new)

                            activity_new.add_student(student)                   
                            random_student.add_activity(activity)
                            
                    

                            malus_list.append(maluscount)  
                            changed_student += 1

                            print(malus_calc.malus_calc(student_data,activity_list), maluscount)
                            
                            if malus_calc.malus_calc(student_data,activity_list) > maluscount:
                                
                                changed_student -= 1
                                malus_list.pop()

                                activity.remove_student(random_student)
                                activity_new.remove_student(student)
                                student.remove_activity(activity_new)
                                random_student.remove_activity(activity)


                                activity.add_student(student)
                                activity_new.add_student(random_student)
                                student.add_activity(activity)
                                random_student.add_activity(activity_new)
                        

                            

    
    return changed_student,malus_list,student_data,activity_list,week_data, course_list

solution = single_loop()

for index, item in enumerate(solution[2]):
    if len(item.students) == 0:
        del solution[2][index]

for day in solution[3].schoolweek:
    for time in day.time_slots:
        for room in time.room_slots:
            for index, item in enumerate(room.scheduled_activity):
                if item != "empty":
                    if len(item.students) == 0:
                        room.scheduled_activity[index] = "empty"
                        room.flag = False
                
                        
# [student_data,courses_list,activity_list,week_data]

# print("hi")

for student_1 in solution[0]:
    print(student_1.name,)
    for i in student_1.activities:
        print(i.name,i.type)

for activity in solution[2]:
    print("hi")
    print(activity.name, activity.type)
    print(activity.capacity, len(activity.students))
    

changed_activity,malus_list,student_data,activity_list,week_data,course_list = course_switch_emptyslot(1,solution)
changed_activity,malus_list,student_data,activity_list,week_data,course_list = course_switch(1,solution)
changed_student,malus_list,student_data,activity_list,week_data,course_list = student_switch(1,solution)
changed_activity,malus_list,student_data,activity_list,week_data,course_list = course_switch_emptyslot(1,solution)
changed_activity,malus_list,student_data,activity_list,week_data,course_list = course_switch(1,solution)
changed_student,malus_list,student_data,activity_list,week_data,course_list = student_switch(1,solution)


for student_1 in solution[0]:
    print(student_1.name,)
    for i in student_1.activities:
        print(i.name,i.type)

for activity in solution[2]:
    print("hi")
    print(activity.name, activity.type)
    print(activity.capacity, len(activity.students))
    


print("final malus count: {}".format(malus_calc.malus_calc(student_data,activity_list)))
visuals.plotter(week_data)

plt.plot(np.arange(changed_student), malus_list)



plt.xlabel("Amount of activity switches")
plt.ylabel("Maluspoints")
plt.show()

# for student_1 in student_data:
#     print(student_1.name)
#     for i in student_1.activities:
#         print(i.name,i.type)




        
# alles hieronder is om N aantal random roosters te maken



# malus =  9999 
# malus_graph = []

# for i in range(100):
#     loop = single_loop()
#     solution = loop[1]
#     malus_temp = loop[0]
#     malus_graph.append(malus_temp)

#     if malus_temp < malus:
#         malus = malus_temp
#         solution_short = solution


# sys.setrecursionlimit(3000)
# print(malus)
# config_dictionary = {"solution" : solution_short[3], "maluspunten" : malus}

# with open(r"config.dictionary", "rb") as input_file:
#     e = pickle.load(input_file)
#     current_lowest = e["maluspunten"]

# with open('config.dictionary', 'wb') as config_dictionary_file:
 
#   # Step 3
#     if config_dictionary["maluspunten"] < current_lowest: 
#         pickle.dump(config_dictionary, config_dictionary_file)
#     pickle.dump(e, config_dictionary_file)


# visuals.plotter(solution_short[3])


# with open("config.dictionary", "rb") as input_file:
#     e = pickle.load(input_file)
#     print(e)
#     print(e["solution"])
#     print(e["maluspunten"])



# plt.hist(malus_graph, rwidth=0.75, bins = 60);
# plt.show()