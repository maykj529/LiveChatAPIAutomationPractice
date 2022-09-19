import pytest


def inc(a, b):
    return a + b


class TestFun:

    @pytest.mark.may
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b", [(1, 2)])
    def test_positive_integer(self, a, b):
        assert inc(a, b) == 3

    @pytest.mark.may
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b", [(-1, -2)])
    def test_negative_integer(self, a, b):
        assert inc(a, b) == -3

    @pytest.mark.may
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b", [(1, -2)])
    def test_positive_plus_negative(self, a, b):
        assert inc(a, b) == -1

    @pytest.mark.may
    @pytest.mark.smoke
    @pytest.mark.parametrize("a,b", [(1.2, 2.3)])
    def test_decimal(self, a, b):
        assert inc(a, b) == 3.5

    @pytest.mark.may
    @pytest.mark.illegal
    @pytest.mark.parametrize("a,b", [(3, 3)])
    def test_error(self, a, b):
        assert inc(a, b) == 3
