# VISUALISATION OF DATA
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

import schedule
import rooster

val1 = []
val2 = []
val3 = []

week_data = schedule.Week()

fig, axes = plt.subplots(nrows=5, ncols=1, constrained_layout=True)

n = 0

# df = pd.DataFrame({
# })

for k in week_data.day_list():
    
    for i in k.timeslot_list():
        val3.append(i.time)

        for p in i.room_list():
            val1.append(p.number)





    table = axes[n].table(
        cellText = [["" for c in range(7)] for r in range(len(val3))],
        # len(val1)//len(val3)
        rowLabels = val3,
        colLabels = val1,
        rowColours =["pink"] * 5,
        colColours =["pink"] * 7,
        cellLoc ='center',
        loc ='upper left')

    axes[n].set_title(k.day, 
                fontweight ="bold")

    axes[n].set_axis_off()

    # iterate through subjects and put them into table in order

    val3 = []

    n = n + 1

plt.show()