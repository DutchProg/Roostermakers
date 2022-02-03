# Roostermakers

Programmeer Theorie - Lectures & Lesroosters

*Sanae Azzouzi, Jason Clark, Ezra de Cleen*

### Building timetables with digital means 
- - -

<p align="center">
    <img src="images/roostering.jpg " width="200">
</p>

The creation of a timetable for universities and schools is a complicated and difficult problem when it comes to using computer agorithms. To begin with timetables don't have a clear distinction of what can be considered appectable or not acceptible. Partially this is due to all the criteria and elements that are necessary to consider, making it a complete multi-dimensional problem. It's also something that is completely individual to the insitution for which algorithm is being designed (Willemen, 2002).

Often the algorithm only being used as the starting point for the creation of the timetable, where fine tuning is done by hand. Timetable construction, especially for schools is a never ending problem, in which an optimal solution will never be found, every semester the amount of students, classes offered, and teachers available changes. But this is exactly what makes it such an interesting case to examine, which is why people have been doing it for years. Even as such, with the growing amount of students accepted within universities, these algorithms became more and more important for building a timetable schedule. 

In conclusion, we can realise that this won't be an easy problem to solve, and it will require a lot of critical thinking in the development stage to see how successful we are in creating this algorithm. 

### Lectures & Lesroosters case
- - -

As part of the programeer theorie we have chosen the case Lectures & Lesroosters for which we will build a timetable schedule for a group of subjects for the UvA Science Park building. The specific criteria we are given for this case are the following:

- All subjects exist out of activities: lectures and/or tutorials and/or practicals.
- All rooms are available for each subject activity
- For every subject there is a value of E(students) which indicates how many are expected for each subject
- With lectures all students enrolled into that course have to present for the activity 
- A class must fit into a specific timeslot of (9:00-11:00, 11:00-13:00, 13:00-15:00 or 15:00-17:00), with one extra evening slot (17:00-19:00) which is available only for the biggest classroom
- A valid timetable is one in which all acitivities from each subject are given a timeslot with a room
- One class can only be used for one activity at a time

Whilst being a difficult problem, the case offers some relaxation in the things we must take into account when building the timetable; we are only building a schedule for one semester which is weekly repeatable. On top of this, we don't need to consider teachers and lecturers and their scheduling.

Within the context of this case we are given a clear method of analysing what would be considered a good solution, as this is something that is normally hard to measure. The case does this through applying points (known as minus points) for specific scenarios, with the aim that our solution should achieve the least amount of points possible. The scenarios in which we gain these points are:
- 5 points for using the aformentioned evening slot
- 1 point for each subject activity clash each student has
- We want to minimise the amount of free time a student has between subjects, for each single empty slot that occurs between subjects per student, we will gain 1 point. If there are two empty slots for the student, we will gain 3 points. A gap of three empty slots between subjects is not allowed within this structure. Unfortunately, we were unable to eliminate gaps larger than 2 slots, these larger gaps were also given 3 points in our program due to complications we encountered with the coding, and the time pressure in completing the project.

This points system will act as a point of reference upon which we will compare and evaluate our algorithms. 

### Algorithms
- - -

#### Baseline

The baseline for this project was to have a functioning timetable which contained all the activities of all the subjects. So we had to calculate the minimum amount of total combination of lectures, workgroups, and tutorials for each specific activity. Based on this we are able to fill the entire week schedule, by performing a single random loop which puts the activities in random timeslots. This gave us a complete unoptimised timetable. 

This process however is done with constraints: it takes into account the room capacity and ensure that each activity is put in the room with the smallest capacity. On top of this, we aimed to use the night slots as little as possible. However, it may be in later stages that we find combinations where the night slot offers less minus points than without using it. 

#### Algorithm 1: Activity Swap

To improve on this initial baseline result, we used a hill climber algorithm, in which we aim to make small continious incremental changes to get a more optimised solution. This could be done with a swapping method which would then slowly change the position of certain parts of the case. We would compare the points calculated from this swap with the points before this change was implemented. If the number of mins points has decreased or stayed the same, we maintain this new change to the timetable, if not we revert to the previous timetable. We kept changes that did not change the score because this prevents the program from getting stuck in a sub-optimal solution. This is continued for a specified amount of time which is included with the initiation of the algorithm.

The first algorithm therefore was made to swap the activity instances of each subject. The first algorithm works by swapping specific instances of that subject’s activity with an empty timetable slot. 

In the beginning, small changes made massive improvements to the number of minus points, with one change being able to negate numbers in the double digits. However, as this continued, and the timetable became more optimised, the changes became more minimal, and they would also offer smaller and smaller changes. 

After ***N*** amount of changes our total points equated to ***MALUSPUNTEN***

<p align="center">
    <img src="" width="500">
    <br>
    figure 1: results from the hill climber algorithm where activities were swapped with empyu slots
</p>

The next logical step was to begin swapping the activities with other activities, and to compare the minus points based on these changes in a similar way. By processing this algorithm these results were gained:

<p align="center">
    <img src="" width="500">
    <br>
    figure 2: results from the hill climber algorithm where activities were swapped with empyu slots
</p>

To further improve the algorithm, since swapping activities with empty slots offers no more improvements, it would make sense to take it one step at a time to not make it too complicated. 

#### Algorithm 2: Student Swap

Further we also did the same with students, also taking into account which specific activity group they are being placed in, and then moving them between these groups.

student swapping with empty slots

and students swapping with other students

<p align="center">
    <img src=""width="500">
    <br>
    figure 3: results from the hill climber algorithm
</p>

<p align="center">
    <img src=""width="500">
    <br>
    figure 4: results from the hill climber algorithm
</p>

#### Theoretical Optimum

Considering all the academic papers surrounding this topic concerning the difficulty of finding a solution for this problem, we can safely assume the theoretical optimimum, which in this case is a minimum, has to a value above 0. In general due to the individual nature of this problem, and the fact that compromises have to be made in its creation to find something which is as optimal as possible. Since it is not possible to make something which matches both all the students, teachers, and the insititution. For example, with the case we have chosen there is a need to compare whether the evening slot gives more or less points than student conflicts that occur. Each choice adds points to the score, however one adds less than the other. In this sense we can see the problem as being NP-complete (mjv, 2010). Whereby all possible combinations need to be explored to find the list of acceptable solutions. Of course doing this in a way in which we approach all combinations is impractical, therefore, as we did with our approach, we need to slowly approach the factors and elements of the problem one by one. Of course there are also arguments to be made for the application of quantifying aspects of this timetable, as to reduce human individual necessities to simply a scheduling need. But to consider all these factors would make this a near impossible process, so bias and constraints are necessary in a problem like this.

#### Conclusion

With the results, we can be quite certain in saying that we...

reflection on our process
 - backtracking 
 - ambiguity of the project 
 - difficult bugs to fix 
 - keep in mind our intepretation of the results what we are keeping in mind
 - time is not important factor, as long as it doesnt take too long eg 6 months

### Results
- - -

#### Hardware

This is the hardware used when making the calculations

OS: Windows 10 64-bit
<br>
CPU: AMD Ryzen 5 3600 6-core processor
<br>
GPU: NVIDIA GeForce GTX 1660 SUPER
<br>
RAM: 16 gb

#### Data 

|            |      Time     |  Moves  |  Points  |  
|------------|:-------------:|--------:|----------:
| Baseline   |               |         |          |  
| Algorithm 1|               |         |          | 
| Algorithm 2|               |         |          | 


#### Commands & instructions for navigating this project and gaining results

-----------------------------------------------------------------------------------------
A random base solution is created by single_loop

**solution = switch.single_loop():**

-----------------------------------------------------------------------------------------
The switch functions are used to apply a certain algoritm for a certain amount of time.

Switch activity into an empty slot:
**switch.activity_switch_emptyslot(seconds,timeout_amount,change_amount, solution)**

Switch activity with another activity:
**switch.activity_switch(seconds,timeout_amount,change_amount, solution)**

Switch students into an empty slot within an activity:
**switch.student_switch_emptyslot(seconds,timeout_amount,change_amount, solution)**

Switch student with another student in the same type of activity
**switch.student_switch(seconds,timeout_amount,change_amount, solution)**

The arguments of the switch functions are: 
- seconds: The time you want the program to run in seconds

- timeout_amount: after n consecutive attempted changes with no decrease in maluspoints the loop will stop 
(even before the time is up, so set this -1 if you want to run for the full seconds )

- change_amount: If you want the program to stop running after a certain amount of succesfull switches you can input that number, if not put -1.

- solution: just the solution we create with single_loop, the program will continue to use the same schedule if you dont create a new one.

So it is possible to run multiple switch functions in succesion with the same solution.

--------------------------------------------------------------------------------------------
The loop tuner function will loop trough the different algoritm's

**looper.loop_tuner(ac_ac, ac_emp, stud_stud, stud_emp, run_time)**

The arguments of the loper function are:

- activity_with_activity, activity_into_empty, student_with_student, student_into_empty: These are the variables that will determine the amount of ineffective changes one switch function will make before it will switch to the next one. We noticed that using a higher number for the student switches is more effective.

- run_time: this is the total runtime of the program, note that when the runtime is too low to finish the amount of switches with no change, it will divide the runtime between the switch algo'equally.

#### Visualisation

Produces a visual timetable which is based on the list that is produced at the end of the algorithm with the calculated optimum. 

<p align="center">
    <img src="images/timetable_example.jpeg " width="600">
    <br>
    figure 5: visual example of how the table will be visualed
</p>

## References

Algorithm for creating a school timetable. Stack Overflow. (1958, January 1). Retrieved February 2, 2022, from https://stackoverflow.com/questions/2177836/algorithm-for-creating-a-school-timetable 

Almond, M. (1966). An algorithm for constructing university timetables. The Computer Journal, 8(4), 331-340.
Chicago 

Murray, K., Müller, T., & Rudová, H. (2006, August). Modeling and solution of a complex university course timetabling problem. In International Conference on the Practice and Theory of Automated Timetabling (pp. 189-209). Springer, Berlin, Heidelberg.

Willemen, R. J. (2002). School timetable construction : algorithms and complexity. Technische Universiteit Eindhoven. https://doi.org/10.6100/IR553569 
