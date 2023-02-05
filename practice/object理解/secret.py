import time

class Secretary:
    # def __init__(self) -> None:
    #     self.logfile = '_log.txt'
    
    # def write_log(self, text):
    #     log = f'{time.ctime()} : {text} \n'
    #     f = open(self.logfile, 'a')
    #     f.write(log)
    #     f.close()

    # def get_log(self):
    #     f = open(self.logfile, 'r')
    #     log = f.read()
    #     f.close()
    #     return log

    def __init__(self) -> None:
        self.appointment = {}

    def request_appointment(self, when, who):
        if (when in self.appointment):
            return False
        else:
            self.appointment[when] = who
            return True
    
    def get_schedule(self):
        return str(self.appointment)