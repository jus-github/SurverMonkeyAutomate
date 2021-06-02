from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    # driver = webdriver.Firefox(executable_path="D:\\workspace_automation\\drivers\\geckodriver.exe")
    driver = webdriver.Chrome(executable_path="D:\\workspace_automation\\drivers\\chromedriver.exe")
    print("Launching chrome browser ...!!!!")
    return driver

# def setup():
#     if browser=="chrome":
#         driver = webdriver.Chrome(executable_path="D:\\Selenium_Assignment1\\drivers\\chromedriver.exe")
#         print("Launching chrome browser ...!!!!")
#     elif browser=="ie":
#         driver = webdriver.Ie(executable_path="D:\\Selenium_Assignment1\\drivers\\IEDriverServer.exe")
#         print("Launching firefox browser...!!!!")
#     else:
#         driver = webdriver.Firefox(executable_path="D:\\Selenium_Assignment1\\drivers\\geckodriver.exe")
#     return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Survey Monkey'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Jasleen'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)









# pytest -v -s testCases/test_Login.py --browser chrome/firefox ----------RUN
"""
 ---------- # RUN PARALLEL 
 pytest -v -s -n=2 testCases/test_Login.py --browser chrome
 
 pytest -v -s -n=2 testCases/test_Login.py --browser firefox  n=method execute parallely
"""