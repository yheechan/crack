# **CRACK**: automati**C** sea**R**ch for corner test c**A**ses on 0-1 knapsa**CK** problem

# Goal
find a set of input cases (test-suite) that kills all the faulty programs by applying Genetic Algorithm to each input cases in a test-suite.

# CURRENTLY
* generates random solution (input) to 0-1 KNAPSACK problem; at given limits in [baekjoon problem](https://www.acmicpc.net/problem/12865)
* makes a test-suite
* evolves the test-suite to kill faulty programs at its best by applying GA to each input cases.

# Executing Command
```
$ cd src
$ python3 crack.py
```

# Current BUG
* Please fix and handle following bugs (hyunsun)
    * ```discrete_normal_distribution``` function at ```evolution.py``` used within ```crossover``` to select a crossover_point in a normal distribution is quite buggy when possibly the number of elements of a solution is 0. It will basically send value of -1 to the function. For mor detail it produces following bug.
    ```
    /home/yangheechan/23-2/cs454/crack/src/utils/evolution.py:33: RuntimeWarning: invalid value encountered in true_divide
    probabilities = np.exp(-(values - N/2)**2 / (2 * (N/4)**2))
    Traceback (most recent call last):
    File "crack.py", line 20, in <module>
        best_sol = ga.ga(
    File "/home/yangheechan/23-2/cs454/crack/src/utils/ga.py", line 135, in ga
        evolve(
    File "/home/yangheechan/23-2/cs454/crack/src/utils/ga.py", line 44, in evolve
        o1, o2 = evo.crossover(
    File "/home/yangheechan/23-2/cs454/crack/src/utils/evolution.py", line 77, in crossover
        cp2 = discrete_normal_distribution(p2.N-1)
    File "/home/yangheechan/23-2/cs454/crack/src/utils/evolution.py", line 37, in discrete_normal_distribution
        sampled_value = np.random.choice(values, p=probabilities)
    File "mtrand.pyx", line 929, in numpy.random.mtrand.RandomState.choice
    ValueError: probabilities contain NaN
    ```
    * ```budget_proportion``` can sometimes assigne a budget value greater then given budget limit. Please add assertion for validation.

# TODO
* Talk about what visualization (graphs, table, etc.) will be needed for final presentation and report.
* Find needed data (aka, values, informations) to make these visualization

# Tasks
* hyunsun:
    * fix bugs
    * update code for better user interface on running for each ```types```.
    * share this to team so each members can start running experiments
* sumin:
    * implement script for making visualizations
    * receive all the experiments done by each member
    * finalize visualizations
    * possible helpful sites
        * reading json: https://www.geeksforgeeks.org/read-json-file-using-python/
        * reading multiple json in one file: https://pynative.com/python-parse-multiple-json-objects-from-file/
* jaemin & heechan:
    * continue elaboration and thinking with hyunsun and sumin for making our final presentation and report a better quality

# EXPECTATIONS
EXPECT MULTIPLE SHORT ONLINE MEETINGS FOR CLARIFICATIONS BETWEEN EACH OTHER.