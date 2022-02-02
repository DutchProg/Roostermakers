# Roostermakers

Programmeer Theorie - Lectures & Lesroosters

*Sanae Azzouzi, Jason Clark, Ezra de Cleen*

### Building timetables with digital means 
- - -

The creation of a timetable for universities and schools is a complicated and difficult problem when it comes to using computer agorithms. To begin with timetables don't have a clear distinction of what can be considered appectable or not acceptible. Partially this is due to all the criteria and elements that are necessary to consider, making it a complete multi-dimensional problem. It's also something that is completely individual to the insitution for which algorithm is being designed (Willemen, 2002).

With often the algorithm only being used as the starting point for the creation of the timetable, where fine tuning is done by hand. Timetable construction, especially for schools is a never ending problem, in which an optimal solution will never be found, every semester the amount of students, classes offered, and teachers available changes. But this is exactly what makes it such an interesting case to examine, which is why people have been doing it for years. 

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
- We want to minimise the amount of free time a student has between subjects, for each single empty slot that occurs between subjects per student, we will gain 1 point. If there are two empty slots for the student, we will gain 3 points. A gap of three empty slots between subjects is not allowed within this structure.

This points system will act as a point of reference upon which we will compare and evaluate our algorithms. 

### Algorithms
- - -

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
- - -

keep in mind our intepretation of the results what we are keeping in mind

- time is not important factor, as long as it doesnt take too long eg 6 months
- still keep in mind the time -- which hardware gave the time 
- keep in mind how many moves the hill climber did

- how to get these specific results from our project using the 
python3 rooster.py

produces a visual timetable with the timetable which allows for the least amount of maluspunten 


## References

[Almond, M. (1966). An algorithm for constructing university timetables. The Computer Journal, 8(4), 331-340.
Chicago] (https://watermark.silverchair.com/8-4-331.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAscwggLDBgkqhkiG9w0BBwagggK0MIICsAIBADCCAqkGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMllfWq88uUDyTRCGzAgEQgIICegjcHPP3WrvGpLoh1DouU6Xn43pVSlH1gVGwLrB2XC1KemRcWG6WgJUzA86oLBlIn39wK2IceKewr3tMfrJ3dSeLU3bOPfga8Xo6LYLCAu0QqKebPl7JqJjSkw-DlFiiCwMbexbAypd_XrWeqUO8OTknNwQOxuZyLPf5hTpbeeKlf_ceb-ihoNjFIrqOR8N7Kd6qaOten-3260C_-T2MEsvuNHdpnUVKo4F3H_Iex5HOPIyyvqtQ5QpJFmz6ZNtJ1Q3ROMNSKAkzP-jM2i4-_0TIXloI7UpnAo8YCkR7e3kWPOAa0_9UNo2uK64hjIaj5nj9jdg9HmpIClwB8NGerC_NovuR8UJEpCjBfhgeW3ojYcN0xpBll_2qpP6bcINk118XJW9UUNFg_cIOK3vBON3-phOTdyTSACpN2pQP9DvKiscYGJsG9AjRJ8Ywx4KYoKadaiyzWWwcxv7z43zBDs8X5s_TF_rK7r--NAxVTEXO4ppPp2yofc3WDatdcqSYhe6Azcp7VOlBbjxPwVHtlJ3J1b5-GGvM4Dy302yJhset13o2i8JgkM_MgleD7BbYEkaS4PDuP2CT6xtVD_QRgeZVUG9PR7hKMeel9CgikpZHPUn8KEsGFZnhc081ZFZQiPaBI6dMSph3TBIeGSuYLJ5PYFN6W4vgBA1vwgjRdPbECDh1SYIPmP70Ep_voNYyG96x8J33BH1wY_zTcJfANtEcUgsOJIEMfVHSBflXy0R9Z5BoemGeBYt5TT7UnGpvsu5ZXSXRboxkRCsp3CfGJUoEs6Y04NiMRtzqUgsr6dtLi3U4uiBncPXPT7vPztTWOEfNdvgwHwWQV8I)

[Willemen, R. J. (2002). School timetable construction : algorithms and complexity. Technische Universiteit Eindhoven. https://doi.org/10.6100/IR553569] (https://pure.tue.nl/ws/files/1849715/200211248.pdf)
