from tracemalloc import start
import visuals
import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np
import switch_functions as switch
import malus_calc
import time


def looper(ac_ac,ac_emp,stud_stud,stud_emp, run_time):
    solution = switch.single_loop()
    start_time = time.time()
    student_change_tries = 0
    activity_change_tries = 0

    student_changes = 0
    activity_changes = 0
    malus_list_changes = []
    malus_list_tries = []

    while time.time()-start_time < run_time:

        timer = (run_time - (time.time()-start_time) ) /4

        a,b,c,d = switch.activity_switch_emptyslot(timer,ac_emp,solution)

        malus_list_tries.extend(a)
        activity_change_tries += b
        activity_changes += c
        malus_list_changes.extend(d)
        print("malus")
        print(malus_calc.malus_calc(solution[0],solution[2]))

        a,b,c,d = switch.activity_switch(timer,ac_ac,solution)

        malus_list_tries.extend(a)
        activity_change_tries += b
        activity_changes += c
        malus_list_changes.extend(d)
        print("malus")
        print(malus_calc.malus_calc(solution[0],solution[2]))

        a,b,c,d = switch.student_switch(timer,stud_stud,solution)

        malus_list_tries.extend(a)
        student_change_tries += b
        student_changes += c
        malus_list_changes.extend(d)
        print("malus")
        print(malus_calc.malus_calc(solution[0],solution[2]))

        a,b,c,d = switch.student_switch_emptyslot(timer,stud_emp,solution)

        malus_list_tries.extend(a)
        student_change_tries += b
        student_changes += c
        malus_list_changes.extend(d)

        print("next")
        print(malus_calc.malus_calc(solution[0],solution[2]))

        print(len(malus_list_changes),student_changes,activity_changes )
        print(len(malus_list_tries),student_change_tries,activity_change_tries )

    total_changes = student_changes + activity_changes
    total_attempts = student_change_tries + activity_change_tries

    with open("results/total_changes", "wb") as fp:   #Pickling
        pickle.dump(total_changes, fp)

    with open("results/total_attempts", "wb") as fp:   #Pickling
        pickle.dump(total_attempts, fp)

    with open("results/malus_list_changes", "wb") as fp:   #Pickling
        pickle.dump(malus_list_changes, fp)

    with open("results/malus_list_tries", "wb") as fp:   #Pickling
        pickle.dump(malus_list_tries, fp)
    
    return solution[0],solution[2],total_changes,total_attempts, malus_list_changes, malus_list_tries



# solution = switch.single_loop()
# act_changes = 0
# stud_changes = 0
# total_malus = []
# malus_list_2,change_tries,changes,malus_list = switch.activity_switch_emptyslot(30,solution)
# act_changes += change_tries
# total_malus.extend(malus_list_2)
# malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch(30,solution)
# act_changes += change_tries
# total_malus.extend(malus_list_2)
# malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.student_switch(60,solution)
# stud_changes += change_tries
# total_malus.extend(malus_list_2)
# malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch_emptyslot(30,solution)
# act_changes += change_tries
# total_malus.extend(malus_list_2)
# malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch(30,solution)
# act_changes += change_tries
# total_malus.extend(malus_list_2)
# malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.student_switch_emptyslot(60,solution)
# stud_changes += change_tries
# total_malus.extend(malus_list_2)
# total_changes = stud_changes+act_changes


student_data,activity_list,total_changes,total_attempts, malus_list_changes, malus_list_tries = looper(30,30,500,500, 4000)


print("final malus count: {}".format(malus_calc.malus_calc(student_data,activity_list)))
# print("We tried to swap: {}, but were succesful with: {}".format(change_tries, changes))

# visuals.plotter(week_data)

plt.plot(np.arange(total_changes), malus_list_changes)
plt.plot(np.arange(total_attempts), malus_list_tries)

plt.title("30 seconds of activity switching with other activities")
plt.xlabel("Amount of activity switch attempts")
plt.ylabel("Maluspoint decrease per switch attempt")
plt.show()


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