import pytest

try:
    import mylibb
except ImportError:
    mylibb = None

@pytest.mark.skip("Do not run this")
def test_fail():
    assert False

@pytest.mark.skipif(mylibb is None, reason="mylibb is not available")
def test_mylibb():
    assert mylibb.x() == 5

def test_skip_at_runtime():
    if True:
        pytest.skip('skip test')