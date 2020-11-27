# A Command performes instructions to a subject

class Command:

    def execute(self, subject, parameters):

        if self.parameters_are_ok(parameters):

            for parameter in parameters:
                subject = next(self._calculate(subject, parameter))
                
        return subject


    def parameters_are_ok(self, parameters):

        if parameters is not None and isinstance(parameters, str):
            if len(parameters) > 0:
                return True
        return False


    def _calculate(self, subject, parameter):

        x, y, direction = subject
        if parameter == "F":
            if direction == "EAST":
                yield (int(x) + 1, int(y), direction)
        yield (x, y, direction)

