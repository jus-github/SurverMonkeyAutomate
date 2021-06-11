from selenium import webdriver
from  PageObject.Login import Login
# from Utilities.customLogger import LogGen
from Utilities.readProperty import ReadConfig
import Utilities.customLogger as cl
import logging

class Test_001_Login:
    baseUrl= ReadConfig.getApplicationURL()
    username=ReadConfig.getUsereName()
    password=ReadConfig.getPassword()

    logger = cl.customLogger(logging.DEBUG)

    def test_Login(self , setup):
        # self.driver = webdriver.Chrome(executable_path="D:\\Selenium_Assignment1\\drivers\\chromedriver.exe")
        # print("LAunching Chrome...!!!")

        self.logger.info("**************************** Test_001_Login **************************")
        self.logger.info("******Verify Login Test ***************")

        self.driver = setup

        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.nav_click()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title=="Welcome to SurveyMonkey!":
            self.logger.info("******Login  Test Pass  ***************")

            self.driver.close()
            assert True

        else:
            self.logger.error("******Login  Test Fail  ***************")

            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
