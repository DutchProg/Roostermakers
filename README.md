# Roostermakers

Programmeer Theorie - Lectures & Lesroosters

Sanae Azzouzi, Jason Clark, Ezra de Cleen

### Building timetables with digital means 

The creation of a timetable for universities and schools is a complicated and difficult problem when it comes to using computer agorithms. To begin with timetables don't have a clear distinction of what can be considered appectable or not acceptible. Partially this is due to all the criteria and elements that are necessary to consider, making it a complete multi-dimensional problem. It's also something that is completely individual to the insitution for which algorithm is being designed (Willemen, 2002).

With often the algorithm only being used as the starting point for the creation of the timetable, where fine tuning is done by hand.

In conclusion, we can realise that this won't be an easy problem to solve, and it will require a lot of critical thinking in the development stage to see how successful we are in creating this algorithm. 

### Lectures & Lesroosters case

As part of the programeer theorie we have chosen the case Lectures & Lesroosters for which we will build a timetable schedule for a group of subjects for the UvA Science Park building. The specific criteria we are given for this case are the following:

- All subjects exist out of activities: lectures and/or tutorials and/or practicals.
- All rooms are available for each subject activity
- For every subject there is a value of E(students) which indicates how many are expected for each subject
- With lectures all students enrolled into that course have to present
- A class must fit into a specific timeslot of (9:00-11:00, 11:00-13:00, 13:00-15:00 or 15:00-17:00), with one extra evening slot (17:00-19:00) which is available only for the biggest classroom
- A valid timetable is one in which all acitivities from each subject are given a valid timeslot with a room
- One class can only be used for one activity at a time

Whilst being a difficult problem, the case offers some relaxation in the things we must take into account when building the timetable; we are only building a schedule for one semester which is weekly repeatable. On top of this, we don't need to consider teachers and lecturers and their scheduling.

Within the context of this case we are given a clear method of analysing what would be considered a good solution, as this is something that is normally hard to measure. The case does this through applying points (known as minus points) for specific scenarios, with the aim that our solution should achieve the least amount of points possible. The scenarios in which we gain these points are:
- 5 points for using the aformentioned evening slot
- 1 point for each subject activity clash each student has
- We want to minimise the amount of free time a student has between subjects, for each single empty slot that occurs between subjects per student, we will gain 1 point. If there are two empty slots for the student, we will gain 3 points. A gap of three empty slots between subjects is not allowed within this structure.

### Algoritmes 

To begin tackling the problem 


- compare baseline with the initial algorithm and final algorithm
    - keep in mind the bias we apply

#### baseline
randomisation

<img src="images/baseline_results.jpeg " width="500">
REPLACE IMAGE WITH NEW ALGORITHM RESULTS

#### hill climber

multiple hill climber algorithms 

<img src="images/hillclimber_results.jpeg " width="500">
REPLACE IMAGE WITH NEW ALGORITHM RESULTS

- theorertical optimum?? 
    - is it possible?
    - minimum value - can safely assume that a value of 0 is not possible 

What is the theoretical 

### Results

keep in mind our intepretation of the results what we are keeping in mind

- time is not important factor, as long as it doesnt take too long eg 6 months
- still keep in mind the time -- which hardware gave the time 
- keep in mind how many moves the hill climber did

- how to get these specific results from our project using the 
python3 rooster.py

produces a visual timetable with the timetable which allows for the least amount of maluspunten 



### References

Willemen, R. J. (2002). School timetable construction : algorithms and complexity. Technische Universiteit Eindhoven. https://doi.org/10.6100/IR553569 (https://pure.tue.nl/ws/files/1849715/200211248.pdf)