from fcfs import fcfs, clear_results as clear_fcfs
from sjf import sjf, clear_results as clear_sjf
from prepare import prepare
from load_processes import load


def run(select, verbose, wait_time=0.0, amount=100):
    global f, s
    # clear_fcfs()  # clear (previous) FCFS select results
    # clear_sjf()  # clear (previous) SJF select results

    if select != "none":
        prepare(select, amount)

    if select.lower() == "fcfs":
        w = load(select)
        f = fcfs(w, wait_time, verbose)

    elif select.lower() == "sjf":
        w = load(select)
        s = sjf(w, wait_time, verbose)

    elif select.lower() == "both":
        w = load(select)
        f = fcfs(w, wait_time, verbose)
        w = load(select)
        s = sjf(w, wait_time, verbose)

    elif select.lower() == "none":
        pass

    else:
        exit(1)

    return [f, s]


if __name__ == "__main__":
    print("OS scheduling algorithm simulation", "Which algorithm to simulate?", "Possible options are:",
          "'FCFS', 'SJF', 'both'", sep='\n')
    select = input("Your choice: ")
    verbose = input("Should the algorithms be run in verbose mode? (y/n): ")
    try:
        in_chain = int(input("How many processes per chain? (default: 100): "))
    except ValueError:
        in_chain = 100
    try:
        no_chains = int(input("How many chains? (default: 100): "))
    except ValueError:
        no_chains = 100
    wait_time = float(input("Time factor? (1 means real-time, 0.1 means 10 times faster, 0 means no wait, etc.): "))

    if no_chains == 1:
        run(select, verbose, wait_time, in_chain)
    elif no_chains < 1:
        exit(2)
    else:
        fcfs_averages = sjf_averages = 0

        for _ in range(no_chains):
            w = run(select, verbose, wait_time, in_chain)
            fcfs_averages += (w[0])
            sjf_averages += (w[1])

        print("Total FCFS average time:\t", fcfs_averages / no_chains)
        print("Total SJF average time:\t", sjf_averages / no_chains)
