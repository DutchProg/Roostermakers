import random
import math
import schedule
import data_loader as load
import courses
import visuals
import student
import string

student_data = student.get_students()
student_data.pop(0)

# we fetch our course data from the datafile
course_data = load.get_data()

# we initialize our week structure
week_data = schedule.Week()

# we load all the activities into the courses and append the courses into a list
courses_list = courses.get_courses()

# we make a new map to copy our activities in seperately, tis is a shallow copy so we do actually change the main location
activity_shallow = []

total_activity = 0

# we loop trough all our course classes and append the activities, we also count total activities
for i in courses_list:
    for k in i.get_activity_list():

        activity_shallow.append(k)
        total_activity +=1



# we then iterate over all the activities and put it in the first availible slot
# there are 145 slots total for 93 activities 

random_list = random.sample(range(0, 145), total_activity)
counter1 = 0
counter3 = 0 
counter2 = 0
counter23 = 0
#we loop trough the activities
for activity in activity_shallow:
   
    smallest_room_count = 9999

    for day in week_data.day_list():
        
        for timeslot in day.timeslot_list():
            
            for room in timeslot.room_list():
                

                if room.occupied() == False and activity.flag == False and room.max_capacity >= activity.capacity:
                    if room.max_capacity - activity.capacity < smallest_room_count:

                        smallest_room_count = room.max_capacity - activity.capacity
                        smallest_room = room
                        day_small = day
                        timeslot_small = timeslot
                
    counter23 += 1
    smallest_room.add_activity(activity)
      
    activity.set_activity(day_small,timeslot_small,smallest_room)


# per course checken welke studenten de course volgen en ze indelen in de activities, vervolgens de activities opslaan in de student class.
for student_individual in student_data:

    for course in courses_list:
 
        if course.name in student_individual.courses:
            
            course.add_student(student_individual)


# loop om de eerste student even uit te printen als controle.
for i in student_data[0].activities:
    

    print(i.type)
    print(i.name)
    print(i.day.day)
    print(i.time.time)
    print(i.room.number)
    

# This loop prints out found schdule untill 


for k in week_data.day_list():
    #print(k.day)
    for i in k.timeslot_list():
        #print(i.time)
        for p in i.room_list():

            #if p.scheduled_activity[0] != "empty":
                #print(p.scheduled_activity[0].name +" "+ p.scheduled_activity[0].type  + " will be in "+ p.number)
            #else:
                #print(p.number +" is empty")
            nothing=0


Malus_student = 0 
for student_individual in student_data:
    Malus_student += student_individual.malus_calc()

malus_activity = 0 

for activity in activity_shallow:
    if activity.time.night == True:
        malus_activity += 5

print("Totale maluspunten:{}".format(Malus_student+malus_activity))


visuals.plotter(week_data)


