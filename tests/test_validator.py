from command import validator as v
from unittest import TestCase

EAST = "EAST"

class ValidatorTest(TestCase):

    def test_valid_subject(self):
        assert v.Validator.subject_is_ok((2,2,"east"))

    def test_not_integer_x(self):
        assert not v.Validator.subject_is_ok(('a',2,"east"))

    def test_not_valid_direction(self):
        assert not v.Validator.subject_is_ok((0,2,"air"))

    def test_valid_integer_x(self):
        assert v.Validator.subject_is_ok(('0', 2, "east"))

    def test_valid_parameters(self):
        assert v.Validator.parameters_are_ok("fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")

    def test_not_valid_parameters(self):
        assert not v.Validator.parameters_are_ok(2)

    def test_not_valid_parameters_empty(self):
        assert not v.Validator.parameters_are_ok("")