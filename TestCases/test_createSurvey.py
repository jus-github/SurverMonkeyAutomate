import  pytest
from PageObject.CreateSurveyPage import Create
from PageObject.Login import Login
from Utilities.customLogger import LogGen
from Utilities.readProperty import ReadConfig

class Test_002_Create_Survey:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsereName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_create_survey(self,setup):
        self.logger.info("************* Test_002_Create New Survey  **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.nav_click()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info(" *********  LOGIN SUCCESSFULL *****************")
        self.logger.info("******* Starting CREATE SURVEY Test **********")

        self.csur = Create(self.driver)
        self.csur.clickOnCreateSurvey()
        self.csur.clickOnStartFromScratch()
        self.logger.info("************* Providing Survey info **********")
        self.csur.setSurveyName("C")
        self.csur.setSurveyCategory()
        self.csur.clickOnCreate()
        self.logger.info("******* Ending Create Survey test **********")
        self.logger.info("************* ADD PAGE TITLE **********")

        self.csur.AddPageTitle()
        self.csur.setPageTitle('Welcome !!')
        self.csur.setPageDesc('trying to automate my first website...! excited n confused....!!!!')
        self.csur.savePageTitle()

        self.logger.info("************* Page Title successfully added **********")

        self.logger.info("************* Add question  **********")
        self.csur.setQuestion("Enter your email.")
        self.logger.info("*************  added **********")
        # self.csur.chooseAnswerType()
        # self.csur.selectAnswer()
        self.csur.SaveQuesAns()
        self.logger.info("************* First question added **********")
        self.logger.info("*************  NEXT QUESTION CLICK  **********")
        # self.csur.nextQuest()
        # self.csur.setQuestion("How often do you use SurveyMonkey?")
        # self.csur.radio_value("Regularly")
        # self.csur.SaveQuesAns()

        self.driver.close()
        # act_title = self.driver.title
        #
        # if act_title == "SurveyMonkey Design : C":
        #     self.driver.close()
        #     assert True
        #
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "create_survey.png")
        #     self.driver.close()
        #     assert False
