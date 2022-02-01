from data_loader import get_student_data



student_data = get_student_data()

class Student:
    def __init__(self, student_number, name, courses):
        self.student_number = student_number
        self.name = name
        self.courses = courses
        self.activities = []

    def __repr__(self):
        rep = self.name
        return rep

    def get_name(self):
        return self.name

    def get_student_number(self):
        return self.student_number

    def get_courses(self):
        return self.courses
    
    def add_activity(self, activity):
        self.activities.append(activity)

    def remove_activity(self, activity):
        
        for i, item in enumerate(self.activities):
            if (item.id == activity.id and activity.type == item.type and item.name == activity.name):
                del self.activities[i]
            
        

    def malus_calc(self):
        activity_times = []
        activity_dict = {"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[]}
        
        for activity in self.activities:
            index = 0
            activity_times.append((activity.day.day,activity.time.time))

            if activity.time.time == "09:00-11:00":
                index = 1
            if activity.time.time == "11:00-13:00":
                index = 2
            if activity.time.time == "13:00-15:00":
                index = 3
            if activity.time.time == "15:00-17:00":
                index = 4
            if activity.time.time == "17:00-19:00":
                index = 5   
            activity_dict[activity.day.day].append(index)

        malus_points_gap = 0
        
        for key in activity_dict:
            index_previous = None

            # de loop gaat er vanuit dat er geen blokken zijn met meer dan 2 tussenuren, dat mag nml niet.
            for index in activity_dict[key]:
                if index_previous == None:
                    index_previous = index - 1

                if (index - index_previous) == 2:
                    

                    malus_points_gap += 1
                    
                elif (index - index_previous) == 3:
                    
                    malus_points_gap += 3
                index_previous = index
        


        malus_points_double = len(activity_times) - len(set(activity_times))
        malus_points_total = malus_points_gap + malus_points_double

        return malus_points_total   

        
            
        


def get_students():
    students_list = [] 

    for key in student_data:
        first_name = student_data[key][0]
        last_name = student_data[key][1]
        
        courses = []
        for i in range(2, 7):
            if (student_data[key][i]) != '':
                courses.append(student_data[key][i])

        students_list.append(Student(key, first_name + " " +last_name, courses))

    return students_list
