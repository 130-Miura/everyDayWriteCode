import pytest

@pytest.mark.dicttest
def test_something():
    assert True

# @pytest.mark.decttest
def test_someone():
    assert False

def test_else():
    assert True