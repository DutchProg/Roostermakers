


def malus_calc(student_data,activity_list):
    malus_student = 0 

    for student_individual in student_data:
        malus_student += student_individual.malus_calc()

    malus_activity = 0 

    for activity in activity_list:
        if activity.time.night == True:
            malus_activity += 5
    malus_total = malus_student + malus_activity
    return malus_total