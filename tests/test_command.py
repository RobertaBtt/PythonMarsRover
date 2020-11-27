import pytest
from command import command
from unittest import TestCase


class CommandTest(TestCase):

    def setUp(self):
        self.command = command.Command()
        self.object = (4,2,"EAST")

    def test_constructor(self):
         assert self.command != None
         assert isinstance(self.command, command.Command)

    def test_execute(self):

        assert self.command.execute(self.object, "F") == (5,2,"EAST")
        assert self.command.execute(self.object, "FF") == (6,2,"EAST")
        assert self.command.execute(self.object, "FFF") == (7,2,"EAST")