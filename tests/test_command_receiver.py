import pytest
from command import command_receiver
from unittest import TestCase

init_state = (4,2,"EAST")

class CommandReceiverTest(TestCase):

    def setUp(self):
        self.command_receiver = command_receiver.CommandReceiver(init_state)

    def test_constructor(self):
         assert self.command_receiver != None
         assert isinstance(self.command_receiver, command_receiver.CommandReceiver)

    def test_get_state(self):
         assert self.command_receiver.get_state() == (4,2,"EAST")
         assert self.command_receiver.get_state != None

    def test_do_command(self):
          self.command_receiver.do_command("F")
          assert self.command_receiver.get_state() == (7,2,"EAST")
