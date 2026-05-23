import pytest
@pytest.mark.sanity
def test_firstprogram():
    print("Hello Pytest")

@pytest.mark.smoke
def test_greet():
    print('Good Morning')


#cmd: py.pytest -m sanity -v -s
#cmd: py.pytest -m smoke -v -s