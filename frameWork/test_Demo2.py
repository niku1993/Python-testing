import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "hello"
    assert msg == "Hi", "Test failed because strings don't match"

def test_secondProgramCreditCard():
    a = 3
    b = 5
    assert a+2 == b