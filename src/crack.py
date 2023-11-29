from utils import ga

'''
N_MAX = 100
B_MAX = 100000
WEIGHT_MAX = 100000
VALUE_MAX = 10000
'''

N_MAX = 10
B_MAX = 10000
WEIGHT_MAX = 10000
VALUE_MAX = 1000

# **************************
# ********** MAIN **********
# **************************

if __name__ == "__main__":
    best_sol = ga.ga(
        experiment_name='heechan_01',
        tc_size=3, # greater than 2
        gen_limit=4,
        selection=2, # less than tc_size
        cross_rate=1.0,
        cross_at_invalid_rate=0.0,
        mutate_rate=1.0,
        mutate_type_rate=0.2,
        mutate_at_invalid_rate=0.5,
        n_max=N_MAX,
        b_max=B_MAX,
        weight_max=WEIGHT_MAX,
        value_max=VALUE_MAX
    )

