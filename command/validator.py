class Validator:

    directions = ['EAST', 'WEST']

    @staticmethod
    def parameters_are_ok(parameters):
        if parameters is not None and isinstance(parameters, str):
            if len(parameters) > 0:
                return True
        return False

    @staticmethod
    def subject_is_ok( subject):
        if subject is not None and len(subject) == 3:
            try:
                subject = (int(subject[0]), int(subject[1]), subject[2])
            except ValueError:
                return False

            if isinstance(subject[0], int) and  isinstance(subject[1], int) and isinstance(subject[2], str) and  subject[2].upper() in Validator.directions:
                return True
        return False