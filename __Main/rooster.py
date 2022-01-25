import random
import math
import schedule
import data_loader as load
import courses
import visuals
import student


student_data = student.get_students()

for i in student_data:
    print(i.courses)
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

#we loop trough the activities
for activity in activity_shallow:
    spot = random_list[counter1]
    counter1 +=1
    counter2 = 0
    for day in week_data.day_list():
        
        for timeslot in day.timeslot_list():
            
            for room in timeslot.room_list():
                counter2 +=1
                if room.occupied() == False and activity.flag == False and counter2 == spot:
                    counter3+=1
                    activity.set_activity(day.day,timeslot.time,room.number)

                    room.add_activity(activity)


# per course checken welke studenten de course volgen en ze indelen in de activities, vervolgens de activities opslaan in de student class.

for i in courses_list:
    for k in i.get_activity_list():
        
        activity_shallow.append(k)
        total_activity +=1



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



def assign_students():
    for student in student_data:
        for course in student.courses:
            nothing = 0





visuals.plotter(week_data)


