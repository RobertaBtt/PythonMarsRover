from command import command
from unittest import TestCase

EAST = "EAST"

class CommandTest(TestCase):

    def setUp(self):
        self.command = command.Command()
        self.object = (4,2,"EAST")
        self.fake_object = ("broken")

    def test_constructor(self):
         assert self.command != None
         assert isinstance(self.command, command.Command)

    def test_execute(self):
        assert self.command.execute(self.object, "F") == (5,2,EAST)
        assert self.command.execute(self.object, "FF") == (6,2,EAST)
        assert self.command.execute(self.object, "FFF") == (7,2,EAST)

    def test_execute_long_string(self):
        assert self.command.execute(self.object, "F" * 10000) == (10004, 2, EAST)

    def test_execute_none(self):
        assert self.command.execute(self.object, None) == (4, 2, EAST)

    def test_execute_empty(self):
        assert self.command.execute(self.object, "") == (4, 2, EAST)

    def test_execute_not_string(self):
        assert self.command.execute(self.object, 4) == (4, 2, EAST)

    def test_command_on_fake_object(self):
        assert self.command.execute(self.fake_object, "FFF") == "broken"