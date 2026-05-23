#fixture
#is a function which will run before each test case and after each test case
#teardown is a function which will run after each test case

import pytest
@pytest.fixture
def sample_data():
    print("This is the sample data fixture")    #runs before the test case
    data = {"name": "John", "age": 30, "city": "New York"}
    yield data  #yield is used to return the data to the test case and then after the test case execution it will execute the code after yield which is print statement in this case
    print("This is the teardown code for sample data fixture")  #runs after the test case

def test_sample_data(sample_data):
    try:
        assert sample_data["name"] == "John1", "Test failed because name does not match"
        assert sample_data["age"] == 301, "Test failed because age does not match"
        print("Test case executed successfully with sample data fixture")
    except Exception as e:
        print(str(e))
