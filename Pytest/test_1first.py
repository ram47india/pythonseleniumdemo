#any pytest file should start with test_ and any test function(method) should also start with test_
#any code should be written inside the test function only, if we write any code outside the test function then it will be executed before the test execution and it will not be considered as a part of the test case
#Execute all the files available in the folder:
# py.pytest -v -s
#Execute specific file:
# py.pytest <method name> -v -s
# py.pytest test_second -v -s
#Execute particular test case from the file:
# py.pytest -k <testcase name> -v -s
# py.pytest -k program -v -s
# -k : allows us to run test cases that match a specific substring in their names. In this case, it will run all test cases that contain the word "program" in their names.
# -v : stands for verbose mode, which provides more detailed output during test execution. It will show the name of each test case being executed and its result (pass/fail).
# -s : allows us to see the print statements in the console output. By default, pytest captures the output of print statements and does not display them. Using -s will disable this capturing and show the print statements in real-time during test execution.
import pytest

@pytest.mark.skip
def test_firstprogram():
    print("Hello Pytest")

@pytest.mark.smoke
def test_greet():
    print('Good Morning')