#A Command performes instructions to a subject

class Command:

    def do_execute(self, subject, parameters):
        if parameters is not None and isinstance(parameters, str):
            if len(parameters) > 0:
                for parameter in parameters:
                    subject_generator = self._compute(subject, parameter)
                    subject = next(subject_generator)
        return subject

    def _compute(self, subject, parameter):
        x, y, direction = subject
        if parameter == "F":
            if direction == "EAST":
                yield (int(x)+1, int(y), direction)
        yield (x,y,direction)