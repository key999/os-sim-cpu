# shortest job first (next) algorithm
# this is almost the same as fcfs so documentation is only present in places where the algorithms are different
# for whole documentation see fcfs.py


from time import sleep


def sjf(processes, time, verbose="n"):
    total_wait = 0

    # sort processes by execution time
    processes.sort(key=lambda x: x.executeTime)

    for i in range(1, len(processes)):
        processes[i].serviceTime = processes[i - 1].serviceTime + processes[i - 1].executeTime

    for i in processes:
        i.waitTime = i.serviceTime  # - i.arrivalTime
        # set the first process in the chain
        if i.serviceTime == 0:
            i.waitTime = 0

        total_wait += i.waitTime

        with open("sjf_out.csv", "a") as f:
            f.write("{0}\t{1}\t{2}\t{3}\n".format(i.arrivalTime, i.executeTime, i.serviceTime, i.waitTime))

        if verbose != "n":
            print("Now executing:", i.arrivalTime, i.executeTime, i.serviceTime, i.waitTime, sep='\t')
        sleep(i.executeTime * time)

    avg_wait = total_wait / len(processes)

    with open("sjf_out.csv", "a") as f:
        f.write("\t\t\t{0}\n".format(avg_wait))

    print("Avg wait:", avg_wait, sep='\t')
    return avg_wait


def clear_results():
    with open("sjf_out.csv", "w"):
        pass
