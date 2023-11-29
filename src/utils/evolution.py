import random
import numpy as np
import math
from . import solution as sl

def unzip(d):
    weights = [i for i, j in d]
    values = [j for i, j in d]

    return weights, values

def remove_items(items: list, max: int):
    amount = len(items) - max
    rm_items = random.sample(items, amount)

    for item in rm_items:
        items.remove(item)
    
    return items

def cp_sol(s):
    return sl.Solution(s.N, s.budget, s.weights.copy(), s.values.copy(), s.fitness)

def restrict_val(val: int, dir: bool):
    if dir:
        return val - 1
    else:
        return val + 1
    
def discrete_normal_distribution(N):
    # Create a discrete distribution with a normal-like shape
    values = np.arange(N + 1)
    probabilities = np.exp(-(values - N/2)**2 / (2 * (N/4)**2))
    probabilities /= probabilities.sum()

    # Sample from the discrete distribution
    sampled_value = np.random.choice(values, p=probabilities)

    return sampled_value

def budget_proportion(o1, o2, cp1, cp2):
    N1 = o1.N
    N2 = o2.N
    B1 = o1.budget
    B2 = o2.budget
    
    b1 = round(float(B1)*(cp1 + 1)/N1 + float(B2)*(N2 - (cp2 + 1))/N2)
    b2 = round(float(B1)*(N1 - (cp1 + 1))/N1 + float(B2)*(cp2 + 1)/N2)
    
    return b1, b2

# ****************************************************
# ********** Regarding Crossover & Mutation **********
# ****************************************************

def crossover(
        p1, p2,
        cross_rate=0.7,
        at_invalid_rate=0.0,
        n_max=100,
):
    # TODO: Heechan

    if random.random() < cross_rate:
        # print(">> crossver: zipped")
        # zip (weights, values) as a pair -> list of tubles [(w, v) ...]
        t1 = list(zip(p1.weights, p1.values))
        t2 = list(zip(p2.weights, p2.values))

        # randomly select a cross over point to split in uniform distribution
        #cp1 = random.randint(0, p1.N-1)
        #cp2 = random.randint(0, p2.N-1)
        
        # print(">> crossver: select cross point")
        # randomly select a cross over point to split in discrete normal distribution
        cp1 = discrete_normal_distribution(p1.N-1)
        cp2 = discrete_normal_distribution(p2.N-1)

        # print(">> crossver: do crossover")
        # do crossover
        c1 = t1[:cp1] + t2[cp2:]
        c2 = t2[:cp2] + t1[cp1:]

        # print(">> crossover: assertion for valid input")
        # if number of items exceeds N_MAX
        # remove items to satisfy N_MAX
        if len(c1) > n_max:
            if random.random() < at_invalid_rate:
                c1 = remove_items(c1, n_max)
            else:
                c1 = random.sample(c1, n_max)
        if len(c2) > n_max:
            if random.random() < at_invalid_rate:
                c2 = remove_items(c2, n_max)
            else:
                c2 = random.sample(c2, n_max)

        assert(len(c1) <= n_max and len(c2) >= 0)
        assert(len(c2) <= n_max and len(c2) >= 0)

        # print(">> crossover: unzip")
        # unzip cross overed pair
        c1_weights, c1_values = unzip(c1)
        c2_weights, c2_values = unzip(c2)

        # print(">> crossover: copy for new offspring")
        # make an offspring
        o1 = cp_sol(p1)
        o2 = cp_sol(p2)

        # print(">> crossover: update new weights & values")
        # assign cross over weight and profit to offspring
        o1.weights = c1_weights
        o1.values = c1_values
        o2.weights = c2_weights
        o2.values = c2_values

        # print(">> crossover: update budget as porportion")
        # update budget for the offspring in proportion to its N
        o1.budget, o2.budget = budget_proportion(o1, o2, cp1, cp2)

        # print(">> crossover: update length")
        # update N for the offspring to new cross over weight and profit
        o1.N = len(o1.weights)
        o2.N = len(o2.weights)

        # evaluate offspring for new fitness score
        # print(">> crossover: evaluating o1")
        o1.evaluate()
        # print(">> crossover: evaluating o2")
        o2.evaluate()

        return o1, o2
    
    # print(">> crossover: done")
    
    return p1, p2



def mutate(
        s,
        mutate_rate=0.7,
        mutate_type_rate=0.5,
        at_invalid_rate=0.5,
        b_max=100000,
        weight_max=100000,
        value_max=10000
):
    m = cp_sol(s)
    update = False

    # print(">> mutate: mutate budget")
    # mutate budget
    if random.random() < mutate_rate:
        update = True
        if random.random() < mutate_type_rate:
            m.budget += random.choice([-1, 1]) 
            # when mutated budget exceeeds b_max
            if m.budget > b_max or m.budget < 0:
                if random.random() < at_invalid_rate:
                    m.budget = restrict_val(m.budget, (m.budget > b_max))
                else:
                    m.budget = random.randint(0, b_max)
        else:
            m.budget = random.randint(0, b_max)

    assert(m.budget <= b_max and m.budget >= 0)
        

    # Iterate over each element, weights, values
    # print(">> mutate: mutate elements")
    for i in range(m.N):
        if random.random() < mutate_rate:
            update = True
            # Apply a small random change to the gene
            # if value exceeds weight_max, value_max
            # mutate value to satisfy them
            if random.random() < mutate_type_rate:
                m.weights[i] += random.choice([-1, 1])
                if m.weights[i] > weight_max or m.weights[i] < 0:
                    if random.random() < at_invalid_rate:
                        m.weights[i] = restrict_val(m.weights[i], (m.weights[i] > weight_max))
                    else:
                        m.weights[i] = random.randint(0, weight_max)

                m.values[i] += random.choice([-1, 1])
                if m.values[i] > value_max or m.values[i] < 0:
                    if random.random() < at_invalid_rate:
                        m.values[i] = restrict_val(m.values[i], (m.values[i] > value_max))
                    else:
                        m.values[i] = random.randint(0, value_max)
            else:
                m.weights[i] = random.randint(0, weight_max)
                m.values[i] = random.randint(0, value_max)

        assert(m.weights[i] <= weight_max and m.weights[i] >= 0)
        assert(m.values[i] <= value_max and m.values[i] >= 0)
    
    # print(">> mutate: evaluate mutated individual")
    if update:
        m.evaluate()

    return m