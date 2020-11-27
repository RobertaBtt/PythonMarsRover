from . import command
class CommandReceiver:

    def __init__(self, initial_state):
        self._state = initial_state

    def get_state(self):
        return self._state

    def do_command(self, parameters):
        self._state = command.Command().do_execute(self._state, parameters)


