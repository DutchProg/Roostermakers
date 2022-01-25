# VISUALISATION OF DATA
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



def plotter(week_in):
    uber_main = []
    main_list = []
    sub_list = []

    for k in week_in.day_list():
        main_list = []
        for i in k.timeslot_list():
            
            sub_list = []
            for p in i.room_list():
                if len(i.room_list()) != 1:
                    if p.scheduled_activity[0] != "empty":
                        sub_list.append(p.scheduled_activity[0].name +" "+ p.scheduled_activity[0].type)
                    else:
                        sub_list.append(p.scheduled_activity[0])
                else:
                    if p.scheduled_activity[0] != "empty":
                        sub_list = ["empty","empty","empty","empty","empty",p.scheduled_activity[0].name +" "+ p.scheduled_activity[0].type ,"empty"]
                    else:
                        sub_list = ["empty","empty","empty","empty","empty",p.scheduled_activity[0] ,"empty"]
            main_list.append(sub_list)    
        uber_main.append(main_list)


    val1 = []
    val2 = []
    val3 = []


    fig, axes = plt.subplots(nrows=5, ncols=1, constrained_layout=True)

    n = 0

    # df = pd.DataFrame({
    # })
    counter_3 = 0
    for k in week_in.day_list():
        current = uber_main[counter_3]
        counter_3 +=1
        for i in k.timeslot_list():
            val3.append(i.time)

            for p in i.room_list():
                val1.append(p.number)


        table = axes[n].table(
        cellText = current,
        # len(val1)//len(val3)
        rowLabels = val3,
        colLabels = val1,
        rowColours =["pink"] * 5,
        colColours =["pink"] * 7,
        cellLoc ='center',
        loc ='upper left')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        axes[n].set_title(k.day, 
                fontweight ="bold")

        axes[n].set_axis_off()

        # iterate through subjects and put them into table in order

        val3 = []

        n = n + 1

    plt.show()
