from secret import * 

class Manager:
    def __init__(self) -> None:
        self.sara = Secretary()
    
#     def work_a(self):
#         self.sara.write_log('hello')
#         time.sleep(5)
#         self.sara.write_log('hey')
    
#     def work_b(self):
#         print(self.sara.get_log())
        
# if __name__ == '__main__':
#     bob = Manager()
#     bob.work_a()
#     bob.work_b()

    def check_schedule(self):
        schedule = self.sara.get_schedule()
        print(schedule)

    def get_secretary(self):
        return self.sara
    
