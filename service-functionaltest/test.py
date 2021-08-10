import pytest


@pytest.mark.FUNCTIONAL
def test_assert_tuple():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.REGRESSION
def test_assert_contain():
    assert 1 in (1, 2, 3)
    
@pytest.mark.REGRESSION
def test_assert_contain1():
    assert 1 in (1, 2, 3)

@pytest.mark.REGRESSION
def test_assert_contain2():
    assert 2 in (1, 2, 3)
    
@pytest.mark.REGRESSION
def test_assert_contain3():
    assert 3 in (1, 2, 3)


@pytest.mark.CONTRACT
def test_assert_addition():
    assert 1 + 2 == 3
