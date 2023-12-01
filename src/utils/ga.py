import random

from . import solution as sl
from . import evolution as evo
from . import result as rs
from . import test_suite as ts

# *************************************************
# ********** Regarding Genetic Algorithm **********
# *************************************************

def select(k, population):
    # we randomly sample k solutions from the population
    participants = random.sample(population, k)
    # fitness_values = [sl.fitness(p) for p in participants]
    result =  sorted(participants, key=lambda x:x.fitness, reverse=True)[0]
    return result

def evolve(
        test_suite,
        selection=3,
        cross_rate=1.0,
        cross_at_invalid_rate=0.0,
        mutate_rate=0.08,
        mutate_type_rate=0.5,
        mutate_at_invalid_rate=0.5,
        n_max=100,
        b_max=100000,
        weight_max=100000,
        value_max=10000,
        method = 1
    ):
    next_gen = []

    while len(next_gen) < len(test_suite.tc_list):
        print(">> evolving test suite {}/{}".format(len(next_gen), len(test_suite.tc_list)))

        print(">> selection")
        # select the fitter parents
        p1 = select(selection, test_suite.tc_list)
        p2 = select(selection, test_suite.tc_list)

        print(">> crossover")
        # crossover to generate a pair of offspring
        o1, o2 = evo.crossover(
            p1, p2,
            cross_rate=cross_rate,
            at_invalid_rate=cross_at_invalid_rate,
            n_max=n_max,
            b_max=b_max,
            method = method
        )

        print(">> mutation")
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

        print(">> add to new generation")
        next_gen.append(m1)
        next_gen.append(m2)

    test_suite.tc_list.extend(next_gen)
    sorted_list = sorted(test_suite.tc_list, key=lambda x: x.fitness, reverse=True)
    test_suite.tc_list = sorted_list[:test_suite.tc_num]

def ga(
    experiment_name='test_no_name',
    end_criterion=0.9,
    ts_size=5,
    tc_size=5,
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
    value_max=10000,
    method = 1
):
    assert(tc_size > selection)

    # record experiment parameter
    rs.record_parameter({
        "experiment_name": experiment_name,
        "end_criterion": end_criterion,
        "tc_size": tc_size,
        "gen_limit": gen_limit,
        "selection": selection,
        "cross_rate": cross_rate,
        "cross_at_invalid_rate": cross_at_invalid_rate,
        "mutate_rate": mutate_rate,
        "mutate_type_rate": mutate_type_rate,
        "mutate_at_invalid_rate": mutate_at_invalid_rate,
        "n_max": n_max,
        "b_max": b_max,
        "weight_max": weight_max,
        "value_max": value_max,
        "method" : method
    })

    ts_list = []
    # make test_suites
    for i in range(ts_size):
        tc_list = []
        # make test_cases
        for j in range(tc_size):
            tc = sl.random_solution(
                n_max=n_max, b_max=b_max,
                weight_max=weight_max, value_max=value_max
            )
            tc.evaluate()
            tc_list.append(tc)

            print(">> finish making individual {}/{}".format(j+1, tc_size))

        test_suite = ts.Test_Suite(tc_list)
        test_suite.evaluate()

        ts_list.append(test_suite)

        print(">> finish making test suite")

    best_solution = ts_list[random.randrange(ts_size)]
    gen_count = 0

    ts_per_gen = {}
    while gen_count < gen_limit and best_solution.fitness < end_criterion:
        print(">> running generation {}/{}".format(gen_count+1, gen_limit))

        for single_ts in ts_list:
            evolve(
                single_ts,
                selection=selection,
                cross_rate=cross_rate,
                cross_at_invalid_rate=cross_at_invalid_rate,
                mutate_rate=mutate_rate,
                mutate_type_rate=mutate_type_rate,
                mutate_at_invalid_rate=mutate_at_invalid_rate,
                n_max=n_max,
                b_max=b_max,
                weight_max=weight_max,
                value_max=value_max,
                method = method
            )
            test_suite.evaluate()
            rs.record_individuals(experiment_name, test_suite, gen_count+1, gen_limit)

        gen_count += 1
    
    return test_suite