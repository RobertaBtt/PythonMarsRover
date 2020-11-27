import pytest
from command import command

def test_constructor():
    c = command.Command()
    assert isinstance(c, command.Command)

def test_get_coordinates():
    c = command.Command()
    assert c.get_coordinates() == (4,2,"EAST")
