import pytest
from selenium import webdriver
import os
driver = None


@pytest.fixture(scope="class")
# @pytest.fixture()
def setup():
    print("This is the setup method to execute before each test case")
    yield
    print("This is the teardown method to execute after each test case")

@pytest.fixture()
def dataload():
    print("User profile data is created")
    return["Ram","Kumar","Testmail@mail.com","9876543210"]

@pytest.fixture(params=[("chrome","windows"),("firefox","linux"),("safari","mac")])
def crossbrowser(request):
    return request.param

@pytest.fixture(scope = "function")
def browserinstance():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver #yield is used to return the driver instance to the test case and then after the test case execution it will execute the code after yield which is driver.close() in this case

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser name to run the tests")

@pytest.fixture(scope = "function")
def browseroptioninstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # To start the browser maximized
        # chrome_options.add_argument("--headless=new")  # To run browser in headless mode
        chrome_options.add_argument("--ignore-certificate-errors")  # Applicable to Windows OS only
        chrome_options.add_argument("--incognito")  # To open browser in incognito mode
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
    elif browser_name == "firefox":
         driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file( file_name )