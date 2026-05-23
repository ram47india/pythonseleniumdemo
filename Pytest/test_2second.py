#Grouping test cases
#you can mark(tag) tests "@pytest.mark.smoke" then execute with "-m" option to run only smoke tests
# py.pytest -m smoke -v -s
#you can skip test cases using "@pytest.mark.skip" and you can also skip test cases based on some condition using "@pytest.mark.skipif(condition, reason)"
# py.pytest -v -s
#Execute without status update in report(used for other dependency test cases)
# "@pytest.mark.xfail" : it will execute the test case but it will not be considered as a failed test case even if it fails, it will be considered as an expected failure
# py.pytest -v -s

import pytest
@pytest.mark.smoke
def test_secondprogram():
    msg = "Hello Pytest"
    assert msg == "Hello Pytest", "Test failed because strings do not match"

@pytest.mark.xfail
def test_secondextra():
    num1 = 10
    num2 = 20
    assert num1 + num2 == 30, "Test failed because the sum does not match"