import random
import schedule
import courses
import student
import malus_calc
import numpy as np
import time

# this function will create a random week schedule with all students in their corresponding classes.
# this random schedule will be used as a starting point for other algoritms
def single_loop():
    student_data = student.get_students()
    student_data.pop(0)

    # we initialize our week structure
    week_data = schedule.Week()

    # we load in the courses and activities
    course_and_activity = courses.get_courses()

    # we load in the courses into a  seperate list
    courses_list = course_and_activity[0]

    # we make a new map to copy our activities in seperately, since these need to be scheduled
    activity_list = course_and_activity[1]

    #we shuffle the activities, so our base schedule will be semi-random (explained later)
    random.shuffle(activity_list)

    # this loop will intialize the week structure with our activities
    for activity in activity_list:
        
        # this is a arbitrary high number to keep track of the smalles possible room for a certain activity
        # this is the only not random part, it would be weird to have a tutorial with 10 people in C0.110
        smallest_room_count = 9999
        
        # for every day in the week
        for day in sorted(week_data.day_list(),key=lambda _: random.random()):
            
            # and every timeslot of the day
            for timeslot in sorted(day.timeslot_list(),key=lambda _: random.random()):
                
                # and every possible room can be used once per timeslot
                for room in sorted(timeslot.room_list(),key=lambda _: random.random()):
                    
                    # we check if the room is oocupied, and if it fits
                    if room.occupied() == False and activity.flag == False and room.max_capacity >= activity.capacity:
                        
                        # we then check if this is indeed the smalles possible room for this activity
                        if room.max_capacity - activity.capacity < smallest_room_count:
                            
                            # we then check if the room is a night slot or not
                            if  room.night == False:
                                
                                smallest_room_count = room.max_capacity - activity.capacity
                                smallest_room = room
                                day_small = day
                                timeslot_small = timeslot

                            if room.night == True:
                                
                                backup_room = room
                                day_small_backup = day
                                timeslot_small_backup = timeslot
        
        # if we indeed found a non nightslot room we will use that room for the activity
        if smallest_room_count != 9999:
            smallest_room.add_activity(activity)
            activity.set_activity(day_small,timeslot_small,smallest_room)

        # if not, we have to use the night slot
        else:
            
            activity.set_activity(day_small_backup,timeslot_small_backup,backup_room)


    # So when all the activities are planned, we can start adding students to the activities they are supposed to follow.
    for student_individual in student_data:

        for course in courses_list:
    
            if course.name in student_individual.courses:
                
                course.add_student(student_individual)

    return [student_data,courses_list,activity_list,week_data]

# switches a activity into a empty slot
def activity_switch_emptyslot(seconds,timeout_amount, change_amount, solution):

    # we initialize our data in more easy to understand variables
    student_data = solution[0]
    course_list =  solution[1]
    activity_list = solution[2]
    week_data = solution[3]

    # we will keep track of how many activities we switched up
    changed_activity = 0
    change_tries = 0
    # we also keep track of our malus points, so we can plot as function of swaps
    malus_list = []
    malus_list_2 = []
    malus_list_3 = []

    timeout = time.time() + seconds
    malus_timeout = 0
    maluscount = 0
    malus_start = malus_calc.malus_calc(student_data,activity_list)

    while time.time() < timeout:
        
        # every time we choose a random activity to switch into an empty slot
        for activity in sorted(activity_list,key=lambda _: random.random()):
            
            if time.time() < timeout:
                
                if changed_activity % 100 == 0:
                    print("Swapped {} activities into an empty slot in {} tries".format(changed_activity,change_tries))
                # we save the current malus points, so we can track if a change is positive
                if changed_activity == change_amount:
                    return malus_list_2 ,change_tries, changed_activity,malus_list
                # this loop will leave if we reach a certain amount of consecutive non imprioving changes
                if maluscount == malus_calc.malus_calc(student_data,activity_list):
                    malus_timeout += 1
                   
                    if malus_timeout == timeout_amount:
                        return malus_list_2 ,change_tries, changed_activity,malus_list
                else:
                    malus_timeout = 0
                maluscount = malus_calc.malus_calc(student_data,activity_list)
                
                # we save the current room and timeslot and day the activity is scheduled
                current_room = activity.room
                current_timeslot = activity.time
                current_day = activity.day
                
                changed = False

                # we choose a random day
                for day in sorted(week_data.day_list(),key=lambda _: random.random()):
                    
                    # a random timeslot
                    for timeslot in sorted(day.timeslot_list(),key=lambda _: random.random()):
                        
                        # and a random room
                        for room in sorted(timeslot.room_list(),key=lambda _: random.random()):
                            
                            # if the room is empty and the activity fits and the activity hasnt been changed before we swap it
                            if room.occupied() == False and room.max_capacity >= activity.capacity and changed == False:
                                
                                # we remove the activity from current room and add it to the new
                                current_room.remove_activity()
                                room.add_activity(activity)
                                activity.set_activity(day,timeslot,room)

                                # we keep track of the change to our maluspoints
                                changed = True
                                malus_list.append(maluscount)  
                                malus_list_2.append(maluscount)
                                changed_activity += 1
                                change_tries += 1
                                malus_list_3.append((malus_start-maluscount)/change_tries)

                                # if the swap gives more maluspoints than before, we revert the change and look for another room
                                if malus_calc.malus_calc(student_data,activity_list) > maluscount:
                                    changed = False
                                    changed_activity -= 1
                                    malus_list.pop()
                                    room.remove_activity()
                                    current_room.add_activity(activity)
                                    activity.set_activity(current_day,current_timeslot,current_room)
                                
                                
                                


    return malus_list_2 ,change_tries, changed_activity,malus_list

# switches two activities with eachother
def activity_switch(seconds,timeout_amount,change_amount, solution):
    # we initialize our data in more easy to understand variables
    student_data = solution[0]
    course_list =  solution[1]
    activity_list = solution[2]
    week_data = solution[3]

    # we will keep track of how many activities we switched up
    changed_activity = 0
    change_tries = 0
    # we also keep track of our malus points, so we can plot as function of swaps
    malus_list = []
    malus_list_2 = []
    malus_list_3 = []

    malus_timeout = 0
    maluscount = 0
    timeout = time.time() + seconds
    malus_start = malus_calc.malus_calc(student_data,activity_list)
    while time.time() < timeout:

        # we choose our activity to switch with another 
        for activity_1 in sorted(activity_list,key=lambda _: random.random()):
            # print every 100 swaps
            
            if time.time() < timeout:
                if changed_activity % 100 == 0:
                    print("Swapped {} activities with another in {} tries".format(changed_activity,change_tries))
                
                if changed_activity == change_amount:
                    return malus_list_2 ,change_tries, changed_activity,malus_list
                # this loop will leave if we reach a certain amount of consecutive non imprioving changes
                if maluscount == malus_calc.malus_calc(student_data,activity_list):
                    malus_timeout += 1
                    
                    if malus_timeout == timeout_amount:
                        return malus_list_2 ,change_tries, changed_activity,malus_list
                else:
                    malus_timeout = 0
                # we save the current malus points, so we can track if a change is positive
                maluscount = malus_calc.malus_calc(student_data,activity_list)

                # we save the current room and timeslot and day the activity is scheduled
                current_room = activity_1.room
                current_timeslot = activity_1.time
                current_day = activity_1.day# we save the current room and timeslot and day the activity is scheduled

                changed = False

                for day in sorted(week_data.day_list(),key=lambda _: random.random()):
                    
                    for timeslot in sorted(day.timeslot_list(),key=lambda _: random.random()):
                        
                        for room in sorted(timeslot.room_list(),key=lambda _: random.random()):
                            
                            # we choose a random day, time and room and check if it indeed has another activity in it
                            if room.occupied() == True and room.max_capacity >= activity_1.capacity and changed == False:
                                
                                # we save the activity in the random room
                                activity_2 = room.scheduled_activity[0]

                                # we add the new activities (overwrites the last, only 1 possible per room)
                                room.add_activity(activity_1)
                                current_room.add_activity(activity_2)

                                # we also update the activity information
                                activity_1.set_activity(day,timeslot,room)
                                activity_2.set_activity(current_day,current_timeslot,current_room)

                                changed = True

                                # we update the malus information and changed tracker
                                malus_list.append(maluscount)
                                malus_list_2.append(maluscount)  
                                changed_activity += 1
                                change_tries += 1
                                malus_list_3.append((malus_start-maluscount)/change_tries)
                                # if the swap gives more maluspoints than before, we revert the change and look for another room
                                if malus_calc.malus_calc(student_data,activity_list) > maluscount:
                                    changed = False
                                    changed_activity -= 1
                                    malus_list.pop()

                                    # we change back the activities in the rooms
                                    room.add_activity(activity_2)
                                    current_room.add_activity(activity_1)

                                    # and room information in the activity class
                                    activity_1.set_activity(current_day,current_timeslot,current_room)
                                    activity_2.set_activity(day,timeslot,room)
        
    return malus_list_2,change_tries, change_amount,malus_list

# changes 1 activity of 1 random student with another student in the same type of activity
def student_switch(seconds,timeout_amount,change_amount, solution):

    # we initialize our data in more easy to understand variables
    student_data = solution[0]
    course_list =  solution[1]
    activity_list = solution[2]
    week_data = solution[3]
    
    # we will keep track of how many students we switched up
    changed_student = 0
    change_tries = 0
    # we also keep track of our malus points, so we can plot as function of swaps
    malus_list = []
    malus_list_2 = []
    malus_list_3 = []

    malus_timeout = 0
    maluscount = 0
    malus_start = malus_calc.malus_calc(student_data,activity_list)
    timeout = time.time() + seconds
    while time.time() < timeout:

        # print every 100 swaps
        if changed_student % 100 == 0:
            
            print("Swapped {} students with other students in {} tries".format(changed_student,change_tries))

        if changed_student == change_amount:
                    return malus_list_2 ,change_tries, changed_student,malus_list

        # this loop will leave if we reach a certain amount of consecutive non imprioving changes
        if maluscount == malus_calc.malus_calc(student_data,activity_list):
            malus_timeout += 1
            
            if malus_timeout == timeout_amount:
                return malus_list_2 ,change_tries, changed_student,malus_list
        else:
            malus_timeout = 0
        # every time we choose a random student to switch with another
        student = random.choice(student_data)

        # we save the current malus points, so we can track if a change is positive
        maluscount = malus_calc.malus_calc(student_data,activity_list)

        changed = False

        # we choose a random activity that the student follows
        for activity in sorted(student.activities,key=lambda _: random.random()):
                
                # we check the activities for same type of activity  
                for activity_new in activity_list:
                    if changed == False:
                        # check if we found one
                        if activity.name == activity_new.name and activity.type == activity_new.type and student not in activity_new.students:
                            
                            # we choose a random student in the newly found activity
                            random_student = random.choice(activity_new.students)
                            
                            # we remove and add the corresponding students
                            activity.remove_student(student)
                            student.remove_activity(activity)
                            activity_new.remove_student(random_student)
                            random_student.remove_activity(activity_new)

                            activity.add_student(random_student)
                            student.add_activity(activity_new)
                            activity_new.add_student(student)                   
                            random_student.add_activity(activity)

                            # we keep track of the change to our maluspoints
                            changed = True
                            malus_list.append(maluscount)  
                            malus_list_2.append(maluscount)
                            changed_student += 1
                            change_tries += 1
                            malus_list_3.append((malus_start-maluscount)/change_tries)
                            if malus_calc.malus_calc(student_data,activity_list) > maluscount:

                                # we revert the changed to malus tracking
                                changed_student -= 1
                                malus_list.pop()
                                changed = False

                                # we then revert the changed to our activities and students
                                activity.remove_student(random_student)
                                activity_new.remove_student(student)
                                student.remove_activity(activity_new)
                                random_student.remove_activity(activity)

                                activity.add_student(student)
                                activity_new.add_student(random_student)
                                student.add_activity(activity)
                                random_student.add_activity(activity_new)

                                

    return malus_list_2,change_tries,changed_student,malus_list



def student_switch_emptyslot(seconds,timeout_amount,change_amount, solution):

    # we initialize our data in more easy to understand variables
    student_data = solution[0]
    course_list =  solution[1]
    activity_list = solution[2]
    week_data = solution[3]
    
    # we will keep track of how many students we switched up
    changed_student = 0
    change_tries = 0
    # we also keep track of our malus points, so we can plot as function of swaps
    malus_list = []
    malus_list_2 = []
    malus_list_3 = []
    maluscount = 0
    malus_timeout = 0
    malus_start = malus_calc.malus_calc(student_data,activity_list)
    timeout = time.time() + seconds
    while time.time() < timeout:

        # print every 100 swaps
        if changed_student % 100 == 0:
            print("Swapped {} students into a activity with capacity in {} tries".format(changed_student,change_tries))

        if changed_student == change_amount:
                    return malus_list_2 ,change_tries, changed_student,malus_list
        # this loop will leave if we reach a certain amount of consecutive non imprioving changes
        if maluscount == malus_calc.malus_calc(student_data,activity_list):
            malus_timeout += 1
            
            if malus_timeout == timeout_amount:
                return malus_list_2 ,change_tries, changed_student,malus_list
        else:
            malus_timeout = 0
        # every time we choose a random student to switch with another
        student = random.choice(student_data)

        # we save the current malus points, so we can track if a change is positive
        maluscount = malus_calc.malus_calc(student_data,activity_list)

        changed = False

        # we choose a random activity that the student follows
        for activity in sorted(student.activities,key=lambda _: random.random()):
                
                # we check the activities for same type of activity  
                for activity_new in activity_list:

                    if changed == False:

                        # check if we found one
                        if activity.name == activity_new.name and activity.type == activity_new.type and student not in activity_new.students and len(activity_new.students) < activity_new.capacity :
                            
                            
                            # we remove and add the corresponding students
                            activity.remove_student(student)
                            student.remove_activity(activity)

                            student.add_activity(activity_new)
                            activity_new.add_student(student)                   
                        

                            # we keep track of the change to our maluspoints
                            changed = True
                            malus_list.append(maluscount)
                            malus_list_2.append(maluscount) 
                            
                            changed_student += 1
                            change_tries += 1
                            malus_list_3.append((malus_start-maluscount)/change_tries) 
                            if malus_calc.malus_calc(student_data,activity_list) > maluscount:

                                # we revert the changed to malus tracking
                                changed_student -= 1
                                malus_list.pop()
                                changed = False

                                # we then revert the changed to our activities and student 
                                activity_new.remove_student(student)
                                student.remove_activity(activity_new)

                                activity.add_student(student)
                                student.add_activity(activity)
                                

                                

    return malus_list_2,change_tries,changed_student,malus_list
