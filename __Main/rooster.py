import visuals
import pickle
import sys
import matplotlib.pyplot as plt
import numpy as np
import switch_functions as switch
import malus_calc

# this function will create a random week schedule with all students in their corresponding classes.
# this random schedule will be used as a starting point for other algoritms

solution = switch.single_loop()

act_changes = 0
stud_changes = 0
total_malus = []
malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch_emptyslot(30,solution)
act_changes += change_tries
total_malus.extend(malus_list_2)
malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch(30,solution)
act_changes += change_tries
total_malus.extend(malus_list_2)
malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.student_switch(60,solution)
stud_changes += change_tries
total_malus.extend(malus_list_2)
malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch_emptyslot(30,solution)
act_changes += change_tries
total_malus.extend(malus_list_2)
malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch(30,solution)
act_changes += change_tries
total_malus.extend(malus_list_2)
malus_list_3,malus_list_2,change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.student_switch_emptyslot(60,solution)
stud_changes += change_tries
total_malus.extend(malus_list_2)
total_changes = stud_changes+act_changes





print("final malus count: {}".format(malus_calc.malus_calc(student_data,activity_list)))
print("We tried to swap: {}, but were succesful with: {}".format(change_tries, changes))

# visuals.plotter(week_data)

plt.plot(np.arange(total_changes), total_malus)
#plt.plot(np.arange(change_tries), malus_list_3)

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