import matplotlib as plt
import visuals
import switch_functions as switch
import looper
import malus_calc
import numpy as np


"""
A random base solution is created by single_loop

the rest of the functions are used to apply a certain algoritm for a certain amount of time.

The arguements of these functions are: seconds,timeout_amount, change_amount, solution
seconds: The time you want the program to run in seconds
timeout_amount: after n consecutive attempted changes with no decrease in maluspoints the loop will stop 
(even before the times, so set this to a high number if y)
"""

"""
solution = single_loop()
switch.activity_switch_emptyslot(seconds,timeout_amount,-1, solution)
switch.activity_switch(seconds,timeout_amount,-1, solution)
switch.student_switch_emptyslot(seconds,timeout_amount,-1, solution)
switch.student_switch(seconds,timeout_amount,-1, solution)
"""


week_data,student_data,activity_list,total_changes,total_attempts, malus_list_changes, malus_list_tries = looper.loop_tuner(30,30,500,500, 30)

print("final malus count: {}".format(malus_calc.malus_calc(student_data,activity_list)))

visuals.plotter(week_data)

plt.plot(np.arange(total_changes), malus_list_changes)
plt.plot(np.arange(total_attempts), malus_list_tries)
plt.title("30 seconds of the combined switches")
plt.xlabel("Amount of total switch attempts")
plt.ylabel("Maluspoints")
plt.show()
