from tracemalloc import start
import pickle
import switch_functions as switch
import malus_calc
import time

# this function will combine all our algortm's
# it will switch between them when a variable amount of hanges with no improvement is met
def loop_tuner(ac_ac,ac_emp,stud_stud,stud_emp, run_time):

    #we start by making a random schedule
    solution = switch.single_loop()
    start_time = time.time()

    student_change_tries = 0
    activity_change_tries = 0
    student_changes = 0
    activity_changes = 0

    malus_list_changes = []
    malus_list_tries = []

    while time.time()-start_time < run_time:

        #This timer just makes sure that every algoritm gets a turn (mostly important for short runs)
        timer = (run_time - (time.time()-start_time) ) /4

        # everything under here are the switch functions and saving it into lists
        a,b,c,d = switch.activity_switch_emptyslot(timer,ac_emp,-1,solution)

        malus_list_tries.extend(a)
        activity_change_tries += b
        activity_changes += c
        malus_list_changes.extend(d)

        a,b,c,d = switch.activity_switch(timer,ac_ac,-1,solution)

        malus_list_tries.extend(a)
        activity_change_tries += b
        activity_changes += c
        malus_list_changes.extend(d)
        
        a,b,c,d = switch.student_switch(timer,stud_stud,-1,solution)

        malus_list_tries.extend(a)
        student_change_tries += b
        student_changes += c
        malus_list_changes.extend(d)
        
        a,b,c,d = switch.student_switch_emptyslot(timer,stud_emp,-1,solution)

        malus_list_tries.extend(a)
        student_change_tries += b
        student_changes += c
        malus_list_changes.extend(d)
        
        print("Our schedule currently has {} minuspoints".format(malus_calc.malus_calc(solution[0],solution[2])))

        print("we made a total of {} changes so far, of which {} student changes and {} activity changes".format(len(malus_list_changes),student_changes,activity_changes) )
        print("we made a total of {} attempted changes so far, of which {} attempted student changes and {} attempted activity changes".format(len(malus_list_tries),student_change_tries,activity_change_tries) )


    total_changes = student_changes + activity_changes
    total_attempts = student_change_tries + activity_change_tries

    # we then save the data we aqquired
    with open("results/total_changes", "wb") as fp:   #Pickling
        pickle.dump(total_changes, fp)

    with open("results/total_attempts", "wb") as fp:   #Pickling
        pickle.dump(total_attempts, fp)

    with open("results/malus_list_changes", "wb") as fp:   #Pickling
        pickle.dump(malus_list_changes, fp)

    with open("results/malus_list_tries", "wb") as fp:   #Pickling
        pickle.dump(malus_list_tries, fp)
    
    return solution[3],solution[0],solution[2],total_changes,total_attempts, malus_list_changes, malus_list_tries
