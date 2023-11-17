import random
import glob

N_MAX = 100
B_MAX = 100000
WEIGHT_MAX = 100000
VALUES_MAX = 10000

class Solution:
    # N: int -> number of item choices
    # weights: list -> list of each item's weight
    # values: list -> list of each item's profit
    # len(weights) and len(pofits) MUST EQuAL to N
    def __init__(self, N, B, weights, value, fitness=0):
        self.N = N
        self.B = B
        self.weights = weights
        self.values = value
        self.fitness = fitness
    
    def evaluate(self):
        self.fitness = fitness(self)
    
    def __str__(self):
        out_str = "====== SOLUTION ======\n"
        out_str += "N: {}\n".format(self.N)
        out_str += "B: {}\n".format(self.B)
        out_str += "weights ({}): {}\n".format(len(self.weights), self.weights)
        out_str += "values ({}): {}\n".format(len(self.values), self.values)
        out_str += "fitness: {}\n".format(self.fitness)
        out_str += "======================"

        return out_str

# generates one random solution
# output: Solution (N, weights, values)
def random_solution():
    N = random.randint(1, N_MAX)
    B = random.randint(1, B_MAX)
    weights = [random.randint(1, WEIGHT_MAX) for i in range(N)]
    values = [random.randint(1, VALUES_MAX) for i in range(N)]
    
    sol = Solution(N, B, weights, values)
    
    return sol
    
def try_solution(solution):
    gt = "dp"
    code = f"""
import {gt}
{gt}.program({solution.N}, {solution.B}, {solution.V}, {solution.W})
    """
    gt_sol = eval(code)
    sample_list = glob.glob("program_*.py")
    sample_list = [s[:-len(".py")] for s in sample_list]
    res_list = []
    for sample in sample_list:
        code = f"""
import {sample}
{sample}.{sample}({solution.N}, {solution.B}, {solution.V}, {solution.W})
        """
        res_list.append(eval(code))
    return gt_sol, res_list

# input: solution
# output: fitness value
def fitness(solution: Solution):
    # TODO: Sumin
    gt_sol, res_list = try_solution(solution)
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

def crossover(p1: Solution, p2: Solution, rate=0.7):
    # TODO: Heechan

    if random.random() < rate:
        # zip (weights, values) as a pair
        t1 = list(zip(p1.weights, p1.values))
        t2 = list(zip(p2.weights, p2.values))

        # randomly select a cross over point to split
        cp1 = random.randint(0, p1.N-1)
        cp2 = random.randint(0, p2.N-1)

        # do crossover
        c1 = t1[:cp1] + t2[cp2:]
        c2 = t2[:cp2] + t1[cp1:]

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
        o1.evaluate()
        o2.evaluate()

        return o1, o2
    
    return p1, p2

def cp_sol(s):
    return Solution(s.N, s.B, s.weights.copy(), s.values.copy(), s.fitness)

def mutate(s: Solution, rate=0.7):
    m = cp_sol(s)

    # Iterate over each element, weights, values
    for i in range(m.N):
        if random.random() < rate:
            # Apply a small random change to the gene
            m.weights[i] += random.choice([-1, 1])
            m.values[i] += random.choice([-1, 1])
    
    m.evaluate

    return m

def ga():
    True


if __name__ == "__main__":
    s1 = random_solution()
    s2 = random_solution()

    print("---initial")
    print(s1)
    print(s2)

    c1, c2 = crossover(s1, s2, rate=1.0)

    print("---after crossover")
    print(c1)
    print(c2)

    m1 = mutate(c1, rate=1.0)
    m2 = mutate(c2, rate=1.0)
    
    print("---after mutation")
    print(m1)
    print(m2)
