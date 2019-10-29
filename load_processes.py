# gets processes from a file


from process import Process
import csv


# loads processes from a csv file written by module prepare.py
# variable txt holds name of the file
# returns a chain (list) of processes (objects)
def load(txt):
    # set name of the file if variable txt does not hold it properly
    if txt.lower() == "fcfs":
        txt = "fcfs_input.csv"
    elif txt.lower() == "sjf" or txt.lower() == "both":
        txt = "sjf_input.csv"

    # reads from the file and appends to variable processes
    # holds data in form of strings
    processes = []
    try:
        with open(txt, "r") as f:
            csv_read = csv.reader(f, delimiter='\t')
            for i in csv_read:
                processes.append(i)
    # on problems with reading the file exits with code 3
    except FileNotFoundError as e:
        print(e)
        exit(3)

    # damn i forgot what this does
    for i in processes:
        for j in range(len(i)):
            i[j] = int(i[j])

    # make a list of objects from the raw input
    objects = []
    for i in processes:
        objects.append(Process(i[0], i[1]))

    # returns a chain (list) of processes (objects)
    return objects
