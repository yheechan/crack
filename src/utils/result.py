from pathlib import Path
import os

def record_results(exp_name, pop, gen_num, gen_limit, pop_lim):
    # record population individuals per generation
    script_file_path = Path(os.path.realpath(__file__))
    src_path = script_file_path.parent.parent

    # make result directory
    result_dir = src_path / "result"
    if not result_dir.exists():
        result_dir.mkdir()

    # make specific experiment directory
    experiment_dir = result_dir / exp_name
    if not experiment_dir.exists():
        experiment_dir.mkdir()
    
    # record current generation's individuals
    ind_txt = experiment_dir / "individuals_{}_{}.txt".format(gen_num, gen_limit)
    with open(ind_txt, "w") as fp:
        for i in range(len(pop)):
            ind_str = "\n***** Individual {}/{} *****\n".format(i+1, pop_lim)
            fp.write(ind_str)
            fp.write(pop[i].__str__())
    
    best_solution = pop[0]

    # record current generations best solution
    result_txt = experiment_dir / "best_solution_per_gen.txt"
    with open(result_txt, "a") as fp:
        gen_str = "\n***** Generation {}/{} *****\n".format(gen_num, gen_limit)
        print(gen_str)
        print(best_solution.__str__())

        fp.write(gen_str)
        fp.write(best_solution.__str__())