import random
import math as math
import schedule
import data_loader as load
import courses

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
for t in activity_shallow:

    for k in week_data.day_list():
        
        for i in k.timeslot_list():
            
            for p in i.room_list():

                if p.occupied() == False and t.flag == False:
                    t.set_activity()
                    p.add_activity(t)
                

# This loop prints out found schdule untill 
for k in week_data.day_list():
    print(k.day)
    for i in k.timeslot_list():
        print(i.time)
        for p in i.room_list():

            if p.scheduled_activity[0] != "empty":
                print(p.scheduled_activity[0].name + " will be in "+ p.number)
            else:
                print(p.number +" is empty")
            