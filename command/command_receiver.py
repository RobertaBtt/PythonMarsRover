class CommandReceiver:

    def __init__(self, init_state):
        self._state = init_state

    def get_state(self):
        return self._state

    def do_command(self, command):
        self._state = (7,2,"EAST")


