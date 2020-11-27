# A Command performs instructions to a subject
from . import validator

class Command:

    def execute(self, subject, parameters):

        if validator.Validator.parameters_are_ok(parameters) and validator.Validator.subject_is_ok(subject):
            for parameter in parameters:
                subject = next(self.__apply_execution(subject, parameter))

        return subject

    # Core logic
    def __apply_execution(self, subject, parameter):
        x, y, direction = subject
        if parameter.upper() == "F":
            if direction.upper() == "EAST":
                yield (int(x) + 1, int(y), direction)
            elif direction.upper() == "WEST":
                yield (int(x) -1, int(y), direction)
        yield (x, y, direction)
