# first come first serve algorithm


# import sleep function
# this is for mimicking actual waiting time
# (to see how long it takes to finish all the processes)
from time import sleep


# main algorithm function
# variable processes holds a chain (list) of processes (objects) to iterate over
# variable time sets waiting time / time scale of waiting
# variable verbose sets if the algorithm outputs verbose info about what it is doing
def fcfs(processes, time, verbose="n"):
    total_wait = 0

    # set service times of every process in the chain
    for i in range(1, len(processes)):
        # service time of the process equals to sum of service and execute time of previous process
        processes[i].serviceTime = processes[i - 1].serviceTime + processes[i - 1].executeTime

    # iterate over processes from input
    for i in processes:
        # calculate wait time for current process
        # if we assume processes arrive at the same time -> wait time is equal to service time
        i.waitTime = i.serviceTime  # - i.arrivalTime
        total_wait += i.waitTime

        # add current process to the end of output file
        with open("fcfs_out.csv", "a") as f:
            f.write("{0}\t{1}\t{2}\t{3}\n".format(i.arrivalTime, i.executeTime, i.serviceTime, i.waitTime))

        # verbosity check and execution if needed
        if verbose != "n":
            print("Now executing:", i.arrivalTime, i.executeTime, i.serviceTime, i.waitTime, sep='\t')

        # mimicking execution of process
        sleep(i.executeTime * time)

    # calculate average wait time for current chain
    avg_wait = total_wait / len(processes)

    # add average wait time of current chain to end of output file
    with open("fcfs_out.csv", "a") as f:
        f.write("\t\t\t{0}\n".format(avg_wait))

    # print and return average wait time
    print("Avg wait:", avg_wait, sep='\t')
    return avg_wait


# function that clears output of the algorithm
def clear_results():
    # opens the file in write - only mode which overwrites contents of the file
    with open("fcfs_out.csv", "w"):
        pass
