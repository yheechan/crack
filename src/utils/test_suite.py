
# ************************************************
# ********** Regarding Test Suite Class **********
# ************************************************

class Test_Suite:
    # tc: list -> list of Solution
    # fitnes: list -> percentage of data killed
    def __init__(self, tc_list, fitness=0.0):
        self.tc_list = tc_list
        self.tc_num = len(self.tc_list)
        self.data_num = len(self.tc_list[0].fitness)
        self.state = [False for i in range(self.data_num)]
        self.fitness = fitness
    
    def evaluate(self):
        self.fitness = fitness(self)
    
    def __str__(self):
        out_str = "====== Test-Suite Info ======\n"
        out_str += "tc_num: {}\n".format(self.tc_num)
        out_str += "data_num: {}\n".format(self.data_num)
        out_str += "state ({}): {}\n".format(len(self.state), self.state)
        out_str += "fitness: {}\n".format(self.fitness)
        out_str += "=============================\n"

        return out_str

# ***************************************
# ********** Regarding Fitness **********
# ***************************************

def fitness(ts):
    new_state = []

    for i in range(ts.tc_num):
        new_state = [x or y for x, y in zip(ts.state, ts.tc_list[i].fitness)]
        ts.state = new_state
    
    true_count = sum(ts.state)

    fitness = (true_count / ts.data_num)
    return fitness
