import random
import os

N_MAX = 100
B_MAX = 100000
WEIGHT_MAX = 100000
VALUE_MAX = 10000

def dp(N: int, B: int, W: list, V: list) -> int:
    if N == 0 or B == 0:
        return 0
    if (W[N-1] > B):
        return dp(N-1, B, W, V)
    else:
        return max(V[N-1] + dp(N-1,B-W[N-1], W, V), dp(N-1, B, W, V))
    

class Solution:
    # N: int -> number of items
    # budget: int -> budget
    # weights: list -> list of each item's weight
    # values: list -> list of each item's profit
    # len(weights) and len(pofits) MUST EQuAL to N
    def __init__(self, N, budget, weights, values, fitness=0):
        self.N = N
        self.budget = budget
        self.weights = weights
        self.values = values
        self.fitness = fitness
    
    def evaluate(self):
        self.fitness = fitness(self)
    
    def __str__(self):
        out_str = "====== SOLUTION ======\n"
        out_str += "N: {}\n".format(self.N)
        out_str += "budget: {}\n".format(self.budget)
        out_str += "weights ({}): {}\n".format(len(self.weights), self.weights)
        out_str += "values ({}): {}\n".format(len(self.values), self.values)
        out_str += "fitness: {}\n".format(self.fitness)
        out_str += "======================"

        return out_str

# generates one random solution
# output: Solution (N, weights, values)
def random_solution():
    N = random.randint(1, N_MAX)
    budget = random.randint(1, B_MAX)
    weights = [random.randint(1, WEIGHT_MAX) for i in range(N)]
    values = [random.randint(1, VALUE_MAX) for i in range(N)]
    
    sol = Solution(N, budget, weights, values)
    
    return sol
    
def try_solution(solution):
    gt = dp(solution.N, solution.budget, solution.weights, solution.values)
    # print(os.listdir("./"))
    sample_list = os.listdir("./data/")
    sample_list = [s for s in sample_list if s.endswith(".py")]
    sample_list = [s.split("/")[-1][:-len(".py")] for s in sample_list]
    res_list = []
    for sample in sample_list:
        exec(f'import data.{sample} as {sample}')
        code = f"{sample}.{sample}({solution.N}, {solution.budget}, {solution.weights}, {solution.values})"
        res_list.append(eval(code))
    return gt, res_list

# input: solution
# output: fitness value
def fitness(solution: Solution):
    # TODO: Sumin
    gt_sol, res_list = try_solution(solution)
    print("gt: ", gt_sol)
    print("res: ", res_list)
    # wrong_distance = sum([(gt_sol - r) for r in res_list])
    wrong_count = sum([1 if gt_sol != r else 0 for r in res_list])
    # a = 1
    # b = 1
    return wrong_count / len(res_list)

def select(k, population):
    # we randomly sample k solutions from the population
    participants = random.sample(population, k)
    fitness_values = [fitness(p) for p in participants]
    result =  sorted(participants, key=lambda x:x.fitness, reverse=False)[0]
    return result

def unzip(d):
    weights = [i for i, j in d]
    values = [j for i, j in d]

    return weights, values

def remove_items(items: list):
    amount = len(items) - N_MAX
    rm_items = random.sample(items, amount)

    for item in rm_items:
        items.remove(item)
    
    return items

def crossover(p1: Solution, p2: Solution, cross_rate=0.7, at_invalid_rate=0.5):
    # TODO: Heechan

    if random.random() < cross_rate:
        # zip (weights, values) as a pair -> list of tubles [(w, v) ...]
        t1 = list(zip(p1.weights, p1.values))
        t2 = list(zip(p2.weights, p2.values))

        # randomly select a cross over point to split
        cp1 = random.randint(0, p1.N-1)
        cp2 = random.randint(0, p2.N-1)

        # do crossover
        c1 = t1[:cp1] + t2[cp2:]
        c2 = t2[:cp2] + t1[cp1:]

        # if number of items exceeds N_MAX
        # remove items to satisfy N_MAX
        if len(c1) > N_MAX:
            if random.random() < at_invalid_rate:
                c1 = remove_items(c1)
            else:
                c1 = random.sample(c1, N_MAX)
        if len(c2) > N_MAX:
            if random.random() < at_invalid_rate:
                c2 = remove_items(c2)
            else:
                c2 = random.sample(c2, N_MAX)

        assert(len(c1) <= N_MAX and len(c2) >= 0)
        assert(len(c2) <= N_MAX and len(c2) >= 0)

        # unzip cross overed pair
        c1_weights, c1_values = unzip(c1)
        c2_weights, c2_values = unzip(c2)

        # make an offspring
        o1 = cp_sol(p1)
        o2 = cp_sol(p2)

        # assign cross over weight and profit to offspring
        o1.weights = c1_weights
        o1.values = c1_values
        o2.weights = c2_weights
        o2.values = c2_values

        # update N for the offspring to new cross over weight and profit
        o1.N = len(o1.weights)
        o2.N = len(o2.weights)

        # evaluate offspring for new fitness score
        # o1.evaluate()
        # o2.evaluate()

        return o1, o2
    
    return p1, p2

def cp_sol(s):
    return Solution(s.N, s.budget, s.weights.copy(), s.values.copy(), s.fitness)

def restrict_val(val: int, dir: bool):
    if dir:
        return val - 1
    else:
        return val + 1


def mutate(s: Solution, mutate_rate=0.7, mutate_type_rate=0.5, at_invalid_rate=0.5):
    m = cp_sol(s)

    # mutate budget
    if random.random() < mutate_rate:
        if random.random() < mutate_type_rate:
            m.budget += random.choice([-1, 1])

            # when mutated budget exceeeds B_MAX
            if m.budget > B_MAX or m.budget < 0:
                if random.random() < at_invalid_rate:
                    m.budget = restrict_val(m.budget, (m.budget > B_MAX))
                else:
                    m.budget = random.randint(0, B_MAX)
        else:
            m.budget = random.randint(0, B_MAX)

    assert(m.budget <= B_MAX and m.budget >= 0)
        

    # Iterate over each element, weights, values
    for i in range(m.N):
        if random.random() < mutate_rate:
            # Apply a small random change to the gene
            # if value exceeds WEIGHT_MAX, VALUE_MAX
            # mutate value to satisfy them
            if random.random() < mutate_type_rate:
                m.weights[i] += random.choice([-1, 1])
                if m.weights[i] > WEIGHT_MAX or m.weights[i] < 0:
                    if random.random() < at_invalid_rate:
                        m.weights[i] = restrict_val(m.weights[i], (m.weights[i] > WEIGHT_MAX))
                    else:
                        m.weights[i] = random.randint(0, WEIGHT_MAX)

                m.values[i] += random.choice([-1, 1])
                if m.values[i] > VALUE_MAX or m.values[i] < 0:
                    if random.random() < at_invalid_rate:
                        m.values[i] = restrict_val(m.values[i], (m.values[i] > VALUE_MAX))
                    else:
                        m.values[i] = random.randint(0, VALUE_MAX)
            else:
                m.weights[i] = random.randint(0, WEIGHT_MAX)
                m.values[i] = random.randint(0, VALUE_MAX)

        assert(m.weights[i] <= WEIGHT_MAX and m.weights[i] >= 0)
        assert(m.values[i] <= VALUE_MAX and m.values[i] >= 0)
    
    # m.evaluate()

    return m

def ga():
    True


if __name__ == "__main__":
    s1 = random_solution()
    s2 = random_solution()

    print("*** initial ***")
    print(s1)
    print(s2)

    for i in range(100000000000):
        print("*** TEST {} ***".format(i))
        s1, s2 = crossover(s1, s2, cross_rate=1.0, at_invalid_rate=0.5)

        print("*** {}: after crossover ***".format(i))
        print(s1)
        print(s2)

        s1 = mutate(s1, mutate_rate=1.0, mutate_type_rate=0.5, at_invalid_rate=0.5)
        s2 = mutate(s2, mutate_rate=1.0, mutate_type_rate=0.5, at_invalid_rate=0.5)

        print("*** {}: after mutation ***".format(i))
        print(s1)
        print(s2)
