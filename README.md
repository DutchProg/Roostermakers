# Roostermakers

Programmeer Theorie - Lectures & Lesroosters

Sanae Azzouzi, Jason Clark, Ezra de Cleen

### Building timetables with digital means 

The creation of a timetable for universities and schools is a complicated and difficult problem when it comes to using computer agorithms. To begin with timetables don't have a clear distinction of what can be considered appectable or not acceptible. Partially this is due to all the criteria and elements that are necessary to consider, making it a complete multi-dimensional problem. 

It's also something that is completely individual to the insitution for which algorithm is being designed.

With often the algorithm only being used as the starting point for the creation of the timetable, where fine tuning is done by hand.

(Willemen, 2002).

Meaning that this won't be an easy problem to solve.

### Lectures & Lesroosters case

As part of the programeer theorie we have chosen the case Lectures & Lesroosters for which we will build a timetable schedule for a group of subjects for the UvA Science Park building. The specific criteria we are given for this case are the following:
- All subjects exist out of activities: lectures and/or tutorials and/or practicals.
- All rooms are available for each subject activity
- For every subject there is a value of E(students) which indicates how many are expected for each subject
- 


Vakken bestaan uit vakactiviteiten: hoorcolleges en/of werkcolleges en/of practica.
Alle zalen zijn voor alledrie collegetypes geschikt.
Voor ieder vak is in de waarde E(studenten) aangegeven hoeveel inschrijvingen er verwacht worden.
Bij hoorcolleges moeten alle ingeschreven studenten ineens bedeeld worden.
Een college duurt van 9:00-11:00, 11:00-13:00, 13:00-15:00 of 15:00-17:00 op een werkdag. Eén zo’n periode van twee uur wordt een tijdsslot genoemd
Een geldig weekrooster is een weekrooster waarvoor aan alle roosterbare activiteiten van ieder vak een tijdsslot met een zaal hebben. We noemen het paar tijdsslot-zaal een zaalslot.
Een zaalslot kan enkel gebruikt worden voor één activiteit.



Whilst being a difficult problem, the case offers some relaxation in the things we must take into account when building the timetable; we are only building a schedule for one semester which is weekly repeatable. 

no teachers and their scheduling - as in whether teachers are available for this many semesters


Within the context of this case we are given a clear method of analysing what would be considered a good solution

### Algoritmes 

randomisation

multiple hill climber algorithms 

- compare baseline with the initial algorithm and final algorithm
    - keep in mind the bias we apply

#### baseline



<img src="images/baseline_results.jpeg " width="500">
REPLACE IMAGE WITH NEW ALGORITHM RESULTS

#### hill climber



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