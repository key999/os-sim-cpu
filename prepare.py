# prepares random processes for the algorithms


from process import Process
from random import randint


# create randomised processes
# variable txt holds name of the file to write to and doubles as a selector (tf?)
# variable amount holds the length of the chain, by default equals to 100
def prepare(txt, amount=100):
    # create random processes
    processes = []
    for i in range(amount):
        processes.append(Process(i, randint(2, 20)))

    # write them to file
    # here is something i dont really understand why i did
    # var txt can hold the exact name as seen in line below  -------------------------\
    # BUT if it doesnt then it is treated differently and instead                     |
    # the processes are written to two files at the same time,                        |
    # which is a weird behaviour that i believe was done for compatibility            |
    # with running two algorithms at the same time                                    |
    # but i should REALLY change this                                                 |
    if txt in ["fcfs_input.csv", "sjf_input.csv"]:  # <-------------------------------/
        with open(txt, "w") as f:
            for i in processes:
                f.write("{0}\t{1}\n".format(i.arrivalTime, i.executeTime))
    else:
        with open("fcfs_input.csv", "w") as f:
            for i in processes:
                f.write("{0}\t{1}\n".format(i.arrivalTime, i.executeTime))

        with open("sjf_input.csv", "w") as f:
            for i in processes:
                f.write("{0}\t{1}\n".format(i.arrivalTime, i.executeTime))

    # return a chain of processes
    return processes
