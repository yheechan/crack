# **CRACK**: automati**C** sea**R**ch for corner test c**A**ses on 0-1 knapsa**CK** problem

CURRENTLY:
* generates random solution (input) to 0-1 KNAPSACK problem; at given limits in [baekjoon problem](https://www.acmicpc.net/problem/12865)
* crossovers a solution
* mutates a sollution

```
$ cd src
$ python3 crack.py
```

# TODO
* hyunsun & jaemin: add datas (source code, program) to ```data/``` directory
    * exclude redundant datas
* sumin: implement fitness function & test it out on given program with ```data/``` directory (soon given by hyunsun)
* heechan:
    * implement random solution generation at given constraints
    * edit crossover & mutation so that it is valid against the given constraints
    * like N changes according to crossover & mutation, update so that budget changes according crossover & mutation