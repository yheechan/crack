# **CRACK**: automati**C** sea**R**ch for corner test c**A**ses on 0-1 knapsa**CK** problem

The CRACK project stands at the forefront of algorithmic testing innovation, aspiring to validate the effectiveness of employing Genetic Algorithms (GAs) in the search for corner test cases within the complex domain of the 0-1 Knapsack Problem. The primary objective of CRACK is to experimentally assess the viability of utilizing Genetic Algorithms in the realm of algorithmic problem solving. Through empirical programs and rigorous experimentation, the project seeks to demonstrate the utility of GAs in uncovering elusive corner cases that may challenge traditional algorithmic solutions. By systematically refining and evolving potential test scenarios, CRACK aims to shed light on the efficiency of this automated approach, paving the way for more resilient and adaptive algorithms in the face of intricate computational challenges.

# How to Run Genetic Algorithm
```
$ cd src/
$ python3 crack.py
```
* To change parameters for genetic algorithm experiment, alter the settings within ```./src/crack.py``` python script.

# Output Results
* Results can be seen in ```./src/result/``` directory.
    * ```individuals_<fomat>/``` directory contains the details of individuals per generation
    * ```test_suite_evolution.<format>``` file contains the information of generations
    * ```parameter.json``` file contains the parameter settings for the experiment

# More Information...
More informations can be found in ```./doc/``` directory, where it contains the slides used during presentation and a final report in PDF format.