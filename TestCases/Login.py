from selenium import webdriver
import time
import unittest
# python -m unittest login.py
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :


        cls.driver = webdriver.Chrome(executable_path="D:\\Selenium_Assignment1\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        self.driver.get("https://www.surveymonkey.com")
        self.driver.find_element_by_xpath("// div[ @ id ='root']//div[@class = 'sm-header--anon__addon-default'] / a[1]").click()
        self.driver.find_element_by_id("username").send_keys("jasleenko")

        self.driver.find_element_by_id("password").send_keys("Test@12345")

        self.driver.find_element_by_xpath("//form[@id = 'sign_in_form']//button[text() = 'LOG IN']").click()

        act_title = self.driver.title

        if act_title == "Welcome to SurveyMonkey!":
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False




    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed ...!")

    if __name__ == '__main__':
        unittest.main()