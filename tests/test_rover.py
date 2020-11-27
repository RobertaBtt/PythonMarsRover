from command import rover
from unittest import TestCase

init_state = (4,2,"EAST")

class RoverTest(TestCase):

    def setUp(self):
        self.rover = rover.Rover(init_state)
        self.rover_no = rover.Rover(None)

    def test_constructor(self):
         assert self.rover != None
         assert isinstance(self.rover, rover.Rover)

    def test_get_state(self):
         assert self.rover.get_state() == init_state
         assert self.rover.get_state != None

    def test_move(self):
          self.rover.move("F")
          assert self.rover.get_state() == (5,2,"EAST")

    def test_move_empty(self):
        self.rover.move(None)
        assert self.rover.get_state() == (4, 2, "EAST")

    def test_move_empty(self):
        self.rover.move("this is not a command")
        assert self.rover.get_state() == (4, 2, "EAST")

    def test_rover_null(self):
        assert self.rover_no.get_state() == None

