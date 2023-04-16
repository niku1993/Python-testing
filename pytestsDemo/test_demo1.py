# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s for logs in output, -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.markname and then run with -m
# you can skip tests with @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - conftest file to generalize
# fixture and make it available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define scope to class only, it will run once before class is initiated and at the end


import pytest



@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])