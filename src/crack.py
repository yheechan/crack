import random
import glob

BUDGET_FIXED = 150
N_RANGE = 30
WEIGHT_RANGE = 20

class Solution:
    # N: int -> number of item choices
    # weights: list -> list of each item's weight
    # profits: list -> list of each item's profit
    # len(weights) and len(pofits) MUST EQuAL to N
    def __init__(self, N, weights, profits):
        self.N = N
        self.weights = weights
        self.profits = profits
        self.fitness = 0
    
    def evaluate(self):
        self.fitness = fitness(self.N, self.items)
    
    def __str__(self):
        out_str = "====== SOLUTION ======\n"
        out_str += "N: {}\n".format(self.N)
        out_str += "weights ({}): {}\n".format(len(self.weights), self.weights)
        out_str += "profits ({}): {}\n".format(len(self.profits), self.profits)
        out_str += "fitness: {}\n".format(self.fitness)
        out_str += "======================"

        return out_str

# generates one random solution
# output: Solution (N, weights, profits)
def random_solution():
    N = random.randint(1, N_RANGE)
    weights = [random.randint(1, WEIGHT_RANGE) for i in range(N)]

    profits = []
    x = [random.random() for i in range(N)]
    for i in range(N):
        profits.append(int(weights[i]*(x[i]*3+0.5)))
    
    sol = Solution(N, weights, profits)
    
    return sol
    
def try_solution(solution):
    gt = "dp"
    code = f"""
import {gt}
{gt}.foo({solution.N}, {solution.weights}, {solution.profits})
    """
    gt_sol = eval(code)
    sample_list = glob.glob("sample_*.py")
    sample_list = [s[:-len(".py")] for s in sample_list]
    res_list = []
    for sample in sample_list:
        code = f"""
import {sample}
{sample}.foo({solution.weights}, {solution.profits})
        """
        res_list.append(eval(code))
    return gt_sol, res_list



# input: solution
# output: fitness value
def fitness(solution: Solution):
    # TODO: Sumin
    gt_sol, res_list = try_solution(solution)
    # wrong distance -> how to penalize?
    # 1. dp의 결과보다 작은 값이 나오는 것보다 dp보다 큰 값이 나오는 게 훨씬 잘못된 것인가?
    #    그냥 절댓값인건지 궁금합니다.
    # 2. 값의 차이가 클수록 edge case인가?
    #    틀린 값을 내놓는데, 결과가 1 차이가 난다고 해서 아쉽거나 그런 건 아닌 것 같습니다.
    wrong_distance = [(gt_sol - r) for r in res_list]
    wrong_count = sum([1 if gt_sol != r else 0 for r in res_list])
    a = 1
    b = 1
    return a * wrong_count + b * wrong_distance

def select(k, population):
    True

def crossover(rate: float, s1: Solution, s2: Solution):
    # TODO: Heechan
    True

def mutate(rate: float, s: Solution):
    # TODO: Heechan
    True

def ga():
    True


if __name__ == "__main__":
    sol = random_solution()
    print(sol)