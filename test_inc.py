import pytest


def add(a, b):
    return a + b


class TestFun:

    @pytest.mark.may
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b", [(1, 2)])
    def test_positive_integer(self, a, b):
        assert add(a, b) == 3

    @pytest.mark.may
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b", [(-11, -22)])
    def test_negative_integer(self, a, b):
        assert add(a, b) == -33

    @pytest.mark.may
    @pytest.mark.logic
    @pytest.mark.parametrize("a,b", [(18, -20)])
    def test_positive_plus_negative(self, a, b):
        assert add(a, b) == -2

    @pytest.mark.may
    @pytest.mark.logic
    @pytest.mark.parametrize("a,b", [(1.2, 2.3)])
    def test_decimal(self, a, b):
        assert add(a, b) == 3.5

    @pytest.mark.may
    @pytest.mark.error
    @pytest.mark.parametrize("a,b", [(3, 3)])
    def test_error(self, a, b):
        try:
            assert add(a, b) == 3
        except BaseException as e:
            print('\n', "wrong result")
