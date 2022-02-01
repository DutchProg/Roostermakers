# Roostermakers

Programmeer Theorie - Lectures & Lesroosters

Sanae Azzouzi, Jason Clark, Ezra de Cleen

### Building timetables with digital means 

The creation of a timetable for universities and schools is a complicated and difficult problem when it comes to using computer agorithms. To begin with timetables don't have a clear distinction of what can be considered appectable or not acceptible. Partially this is due to all the criteria and elements that are necessary to consider, making it a complete multi-dimensional problem. 



Meaning that this won't be an easy problem to solve.

### Lectures & Lesroosters case

As part of the programeer theorie we have chosen the case Lectures & Lesroosters for which we will find a solution. 


Whilst being a difficult problem, the case offers some relaxation in the things we must take into account when building the timetable. 

a repeatable week long schedule for what we can assume to be one semester
no teachers and their scheduling - as in whether teachers are available for this many semesters


Within the context of this case we are given a clear method of analysing what would be considered a good solution

### Algoritmes 

randomisation

multiple hill climber algorithms 

- compare baseline with the initial algorithm and final algorithm
    - keep in mind the bias we apply

#### baseline

<img src="images/baseline_results.jpeg " width="500">

#### hill climber

<img src="images/hillclimber_results.jpeg " width="500">

- theorertical optimum?? 
    - is it possible?
    - minimum value - can safely assume that a value of 0 is not possible 

### Results

keep in mind our intepretation of the results what we are keeping in mind

- time is not important factor, as long as it doesnt take too long eg 6 months
- still keep in mind the time -- which hardware gave the time 
- keep in mind how many moves the hill climber did

- how to get these specific results from our project using the 
python3 rooster.py

produces a visual timetable with the timetable which allows for the least amount of maluspunten 
