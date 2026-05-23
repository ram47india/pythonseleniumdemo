#Fixtues used to execute some code before and after the test execution, it is used to set up the preconditions for the test case and also to clean up after the test case execution. It is a way to provide a fixed baseline upon which tests can reliably and repeatedly execute. It helps in reducing code duplication and also makes the test cases more maintainable. We can use fixtures to set up database connections, create test data, or perform any other setup tasks that are required for the test cases. We can also use fixtures to tear down any resources that were created during the test execution, such as closing database connections or deleting test data.
#Fixtures can be defined at different scopes, such as function, class, module, or session level, depending on how long we want the fixture to be active.
#"conftest" is a special file in pytest that is used to define fixtures that can be shared across multiple test files.
#It allows us to define fixtures in a central location and then use them in any test file without having to import them explicitly. This helps in reducing code duplication and also makes the test cases more maintainable.
#We can define fixtures in the "conftest" file and then use them in any test file by simply referencing the fixture name. The "conftest" file should be placed in the same directory as the test files or in a parent directory, so that it can be discovered by pytest during test execution.



import pytest

@pytest.mark.usefixtures("setup")
class Testfixtureexecution:
    def test_fixture_execution(self):
        print("Executing test case 1")

    def test_fixture_execution2(self):
        print("Executing test case 2")