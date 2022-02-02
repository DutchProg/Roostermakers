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

change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch_emptyslot(500,solution)
change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch(500,solution)
change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.student_switch(500,solution)
change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch_emptyslot(500,solution)
change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.activity_switch(500,solution)
change_tries,changes,malus_list,student_data,activity_list,week_data,course_list = switch.student_switch_emptyslot(500,solution)

print("final malus count: {}".format(malus_calc.malus_calc(student_data,activity_list)))
print("We tried to swap: {}, but were succesful with: {}".format(change_tries, changes))

visuals.plotter(week_data)

plt.plot(np.arange(changes), malus_list)

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