from manager import *
from client import *

bob = Manager()
adam = Client('adam')
adam.set_contact_point(bob.get_secretary())
adam.make_appointment('10:30')