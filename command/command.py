#A Command performed in a subject, giving instructions
class Command:
    def execute(self, subject, parameters):

        if len(parameters) > 0 and isinstance(parameters, str):
            for parameter in parameters:
                subject_generator = self._compute(subject, parameter)
                subject = next(subject_generator)
        return subject

    def _compute(self, subject, parameter):
        x, y, direction = subject
        if parameter == "F":
            if direction == "EAST":
                yield (x+1,y, direction)