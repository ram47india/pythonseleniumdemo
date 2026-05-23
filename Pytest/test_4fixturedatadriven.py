import pytest

@pytest.mark.usefixtures("dataload")
class Testfixturedatadriven:
    def test_fixture_datadriven(self, dataload):
        print("Executing test case 1")
        print(dataload)
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])
        print(dataload[3])
