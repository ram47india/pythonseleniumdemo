#datadriven and parameterizing can be done with return statement in tuple format
#when you define fixture scope to class only, it will run once before class is initiated adn at the end

#HTML reports command => py.test --html = report.html

def test_cross_browser(crossbrowser):
    print("Executing cross browser test case")
    print(crossbrowser)
    print(crossbrowser[0])
    print(crossbrowser[1])