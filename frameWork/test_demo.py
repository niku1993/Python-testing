# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s for logs in output, -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.markname and then run with -m
# you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail

import pytest

def test_firstProgram():
    print ("Hello")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")

def test_secondProgram():
    a = 4
    b = 6
    assert a+2 == b, "Addition match"