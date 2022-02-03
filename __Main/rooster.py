import matplotlib.pyplot as plt
import visuals
import switch_functions as switch
import looper
import malus_calc
import numpy as np


"""
These are the used functions. For instructions on how to use them navigate to the README.md

solution = switch.single_loop():

switch.activity_switch_emptyslot(seconds,timeout_amount,change_amount, solution)

switch.activity_switch(seconds,timeout_amount,change_amount, solution)

switch.student_switch_emptyslot(seconds,timeout_amount,change_amount, solution)

switch.student_switch(seconds,timeout_amount,change_amount, solution)

looper.loop_tuner(ac_ac,ac_emp,stud_stud,stud_emp, run_time)
"""

# This is the looper function, comment out if using a single switch
# change variables to your liking
seconds = 60
ac_ac = 25
ac_emp = 25
stud_stud = 75
stud_emp = 75
week_data,student_data,activity_list,total_changes,total_attempts, malus_list_changes, malus_list_tries = looper.loop_tuner(ac_ac,ac_emp,stud_stud,stud_emp, seconds)


# this is the single switch, comment out if using the looper
# Change the function with any of the single switch functions found at the top of this file
# change variables to your liking
"""
seconds = 30
timeout_amount = -1
change_amount = -1
solution = switch.single_loop()
malus_list_2,change_tries,succesfull_changes,malus_list = switch.student_switch(seconds,timeout_amount,change_amount, solution)
"""


# This will print the final maluscount of our solution aqquired from the looper of switch function.
print("final malus count: {}".format(malus_calc.malus_calc(student_data,activity_list)))

# this will print our schedule
visuals.plotter(week_data)


# this will plot the total changes and the total change attempts on the x axis and the malus points on the y
# this is a result of the looper function, comment this out if you are not using the looper function.
plt.plot(np.arange(total_changes), malus_list_changes)
plt.plot(np.arange(total_attempts), malus_list_tries)
plt.title(f"{seconds} seconds of the combined switches")
plt.xlabel("Amount of total switch attempts")
plt.ylabel("Maluspoints")
plt.show()


# this will plot the total changes and the total change attempts on the x axis and the malus points on the y
# this is a result of the single switich functions, comment this out if you are using the looper function.
"""
plt.plot(np.arange(succesfull_changes), malus_list)
plt.plot(np.arange(change_tries), malus_list_2)
plt.title(f"{seconds} seconds of the single switches")
plt.xlabel("Amount of total switch attempts")
plt.ylabel("Maluspoints")
plt.show()
"""