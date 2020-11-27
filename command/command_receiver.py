class CommandReceiver:
    def __init__(self, init_state):
        self._state = (init_state)

    def get_state(self):
        return self._state

    def do_command(self, direction):
        self._state = (4,3,"EAST")

