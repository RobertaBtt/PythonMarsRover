from . import command

class Rover:

    def __init__(self, initial_state):
        self.__state = initial_state

    def get_state(self):
        return self.__state

    def move(self, parameters):
        self.__state = command.Command().execute(self.__state, parameters)
