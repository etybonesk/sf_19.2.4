import pytest

from calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    # положительные тесты
    def test_adding_success(self):
        print('Положительный тест на сложение.')
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction_success(self):
        print('Положительный тест на вычитание.')
        assert self.calc.subtraction(self, 1, 1) == 0

    def test_multiply_success(self):
        print('Положительный тест на умножение.')
        assert self.calc.multiply(self, 4, 2) == 8

    def test_division_success(self):
        print('Положительный тест на деление.')
        assert self.calc.division(self, 4, 2) == 2
