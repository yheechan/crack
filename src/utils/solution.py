import random
import os

# **********************************************
# ********** Regarding Solution Class **********
# **********************************************

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
        self.ratio = 0.0
    
    def evaluate(self):
        self.fitness = fitness(self)
        self.ratio = sum(self.fitness) / len(self.fitness)

    
    def __str__(self):
        out_str = "====== SOLUTION ======\n"
        out_str += "N: {}\n".format(self.N)
        out_str += "budget: {}\n".format(self.budget)
        out_str += "weights ({}): {}\n".format(len(self.weights), self.weights)
        out_str += "values ({}): {}\n".format(len(self.values), self.values)
        out_str += "fitness: {}\n".format(self.fitness)
        out_str += "ratio: {}\n".format(self.ratio)
        out_str += "======================\n"

        return out_str


# ***********************************************
# ********** Random Solution Generator **********
# ***********************************************

# generates one random solution
# output: Solution (N, weights, values)
def random_solution(n_max, b_max, weight_max, value_max):
    # print(">> random solution: N")
    N = random.randint(1, n_max)
    # print(">> random solution: budget")
    budget = random.randint(1, b_max)
    # print(">> random solution: weights")
    weights = [random.randint(1, weight_max) for i in range(N)]
    # print(">> random solution: values")
    values = [random.randint(1, value_max) for i in range(N)]
    
    # print(">> random solution: Solution")
    sol = Solution(N, budget, weights, values)
    
    return sol


# ***************************************
# ********** DP Correct Answer **********
# ***************************************

def dp(N: int, B: int, W: list, V: list) -> int:
    if N == 0 or B == 0:
        return 0
    if (W[N-1] > B):
        return dp(N-1, B, W, V)
    else:
        return max(V[N-1] + dp(N-1,B-W[N-1], W, V), dp(N-1, B, W, V))


# ***************************************
# ********** Regarding Fitness **********
# ***************************************
    
def try_solution(solution):
    gt = dp(solution.N, solution.budget, solution.weights, solution.values)

    sample_list = os.listdir("./data/")
    sample_list = [s for s in sample_list if s.endswith(".py")]
    sample_list = [s.split("/")[-1][:-len(".py")] for s in sample_list]
    sample_list.sort()

    res_list = []
    for sample in sample_list:
        # print(">> evaluation: trying sample: {}".format(sample))

        exec(f'import data.{sample} as {sample}')
        code = f"{sample}.{sample}({solution.N}, {solution.budget}, {solution.weights}, {solution.values})"

        res = 0
        try:
            res = eval(code)
        except:
            res = -1
        # print("result on {}: {}".format(sample, res))
        res_list.append(res)

    return gt, res_list

# input: solution
# output: fitness value
def fitness(solution):
    # TODO: Sumin
    gt_sol, res_list = try_solution(solution)

    # print("gt: ", gt_sol)
    # print("res: ", res_list)
    # wrong_distance = sum([(gt_sol - r) for r in res_list])

    wrong_count = [True if gt_sol != r else False for r in res_list]
    # print("{} wrong out of {}".format(wrong_count, len(res_list)))
    # final_fitness = wrong_count / len(res_list)

    return wrong_count