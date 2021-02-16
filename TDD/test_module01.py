from calculator import Calculator
import pytest

class TestClass01:
    def test_case01(self):
        calc = Calculator()
        result = calc.add(2, 2)
        assert 4 == result

    def test_case02(self):
        with pytest.raises(ValueError):
            result = Calculator().add(2, 'two')
