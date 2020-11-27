from command import rover
from unittest import TestCase

init_state_east = (4,2,"EAST")
init_state_none = None
init_state_west = (0,0,"west")

class RoverTest(TestCase):

    def setUp(self):
        self.rover = rover.Rover(init_state_east)
        self.rover_no = rover.Rover(init_state_none)
        self.rover_west = rover.Rover(init_state_west)

    def test_constructor(self):
         assert self.rover != None
         assert isinstance(self.rover, rover.Rover)

    def test_get_state(self):
         assert self.rover.get_state() == init_state_east
         assert self.rover.get_state != init_state_none

    def test_move(self):
          self.rover.move("F")
          assert self.rover.get_state() == (5,2,"EAST")

    def test_move_empty(self):
        self.rover.move(None)
        assert self.rover.get_state() == init_state_east

    def test_move_wrong_command(self):
        self.rover.move("this is not a command")
        assert self.rover.get_state() == init_state_east

    def test_rover_null(self):
        assert self.rover_no.get_state() == init_state_none

    def test_from_west(self):
        assert self.rover_west.get_state() == init_state_west

    def test_move_from_west(self):
        self.rover_west.move('ffff')
        assert self.rover_west.get_state() == (-4,0,"west")

