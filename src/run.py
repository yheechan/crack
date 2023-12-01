import subprocess as sp

# Replace 'your_command_here' and 'arg1', 'arg2', etc. with the actual command and arguments
cmd = ['python3', 'crack.py']

for i in range(1, 11, 1):
    exp_nm = "norm_cp_{}".format(i)

    cmd.append(exp_nm)

    print(">> running {}".format(exp_nm))
    process = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.STDOUT, encoding="utf-8")

    while True:
        line = process.stdout.readline()
        if line == '' and process.poll() != None:
            break
        print(line.strip(), flush=True)
    
    print(">> finsihed {}".format(exp_nm))

    cmd.pop()

# x1, x5, x8, x10
# o63, o35, o23, o68, o35, o21