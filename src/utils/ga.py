import random

from . import solution as sl
from . import evolution as evo
from . import result as rs

# *************************************************
# ********** Regarding Genetic Algorithm **********
# *************************************************

def select(k, population):
    # we randomly sample k solutions from the population
    participants = random.sample(population, k)
    fitness_values = [sl.fitness(p) for p in participants]
    result =  sorted(participants, key=lambda x:x.fitness, reverse=True)[0]
    return result


N_MAX = 100
B_MAX = 100000
WEIGHT_MAX = 100000
VALUE_MAX = 10000

def ga(
    experiment_name='test_no_name',
    pop_size=40,
    gen_limit=100,
    selection=3,
    cross_rate=1.0,
    cross_at_invalid_rate=0.0,
    mutate_rate=0.08,
    mutate_type_rate=0.5,
    mutate_at_invalid_rate=0.5,
    n_max=100,
    b_max=100000,
    weight_max=100000,
    value_max=10000
):
    # make initial population at given population size
    population = []
    for i in range(pop_size):
        s = sl.random_solution(
            n_max=n_max, b_max=b_max,
            weight_max=weight_max, value_max=value_max
        )
        s.evaluate()
        population.append(s)
    
    # randomly select a solution as initally best
    gen_count = 0
    best_solution = population[random.randrange(pop_size)]

    # print("selected following formula as initial best solution")
    # print(best_solution)

    while gen_count < gen_limit and best_solution.fitness != 100.0:
        next_gen = []

        while len(next_gen) < len(population):
            # select the fitter parents
            p1 = select(selection, population)
            p2 = select(selection, population)

            # crossover to generate a pair of offspring
            o1, o2 = evo.crossover(
                p1, p2,
                cross_rate=cross_rate,
                at_invalid_rate=cross_at_invalid_rate,
                n_max=n_max
            )

            # mutate offsprings
            m1 = evo.mutate(
                o1,
                mutate_rate=mutate_rate,
                mutate_type_rate=mutate_type_rate,
                at_invalid_rate=mutate_at_invalid_rate,
                b_max=b_max, weight_max=weight_max, value_max=value_max
            )
            m2 = evo.mutate(
                o2,
                mutate_rate=mutate_rate,
                mutate_type_rate=mutate_type_rate,
                at_invalid_rate=mutate_at_invalid_rate,
                b_max=b_max, weight_max=weight_max, value_max=value_max
            )

            next_gen.append(m1)
            next_gen.append(m2)
        
        population.extend(next_gen)
        population = sorted(population, key=lambda x: x.fitness, reverse=True)
        population = population[:pop_size]

        best_solution = population[0]

        rs.record_results(
            exp_name=experiment_name,
            pop=population,
            gen_num=gen_count+1,
            gen_limit=gen_limit,
            pop_lim=pop_size
        )

        gen_count += 1
    
    return best_solution