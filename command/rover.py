from . import command

class Rover:

    def __init__(self, initial_state):
        self._state = initial_state

    def get_state(self):
        return self._state

    def move(self, parameters):
        self._state = command.Command().execute(self._state, parameters)


