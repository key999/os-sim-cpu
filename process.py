# this module defines process class


class Process:
    # initializer, arrival and execute times are needed, service and wait times can be supplied
    # otherwise by default are set to 0
    def __init__(self, arrivalTime, executeTime, serviceTime=0, waitTime=0):
        self.arrivalTime = arrivalTime
        self.executeTime = executeTime
        self.serviceTime = serviceTime
        self.waitTime = waitTime

    # changes the way of printing this object
    # after all it was not needed i think
    def __str__(self):
        return "{0}\t{1}\t{2}\t{3}".format(self.arrivalTime, self.executeTime, self.serviceTime, self.waitTime)
