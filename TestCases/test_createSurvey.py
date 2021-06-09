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
        self.csur.setSurveyName("Survey Form")
        self.csur.setSurveyCategory()
        self.csur.clickOnCreate()
        self.logger.info("******* Ending Create Survey test **********")
        self.logger.info("************* ADD PAGE TITLE **********")

        # self.csur.AddPageTitle()
        # self.csur.setPageTitle('Welcome !!')
        # self.csur.setPageDesc('trying to automate my first website...! excited n confused....!!!!')
        # self.csur.savePageTitle()

        self.logger.info("************* Page Title successfully added **********")

        self.logger.info("************* Add question  **********")
        self.csur.setQuestion("Enter your email.")
        self.logger.info("*************  added **********")
        # self.csur.chooseAnswerType()
        # self.csur.selectAnswer()
        self.csur.SaveQuesAns()
        self.logger.info("************* First question added **********")
        self.logger.info("*************  NEXT QUESTION CLICK  **********")



        # *************  2 Question ****************************
        self.csur.nextQuest()
        self.csur.setQuestion("From When are you using SurveyMonkey?")
        self.csur.select_Date()
        self.csur.SaveQuesAns()

        #
        #
        # self.csur.nextQuest()
        # self.csur.setQuestion("Will recommend SurveyMonkey to your friends / Colleagues? (Radio)")
        # self.csur.radio_value("YES")
        # self.csur.SaveQuesAns()
        #
        # self.csur.nextQuest()
        # self.csur.setQuestion("Comments / Feedback")
        # self.csur.SaveQuesAns()
        #
        # self.csur.nextQuest()
        # self.csur.setQuestion("Did you get meaningful data from survey analysis ?")
        # self.csur.radio_value("YES")
        # self.csur.SaveQuesAns()
        #
        # self.csur.nextQuest()
        # self.csur.setQuestion("How will rate the ease of survey creation?")
        # self.csur.SaveQuesAns()
        #
        #
        #
        # self.csur.nextQuest()
        # self.csur.setQuestion("How often do you use SurveyMonkey ?")
        # self.csur.radio_value("Regularly")
        # self.csur.SaveQuesAns()

        # *************  3 Question ****************************

        self.csur.nextQuest()
        self.csur.setQuestion("Check the Features you like about SurveyMonkey?")
        self.csur.checkbox_value("Question Bank" , "Themes" , "Graphical Result" , "Template Re-usability" , "Collectors")
        self.csur.SaveQuesAns()


        # *************  4 Question ****************************



        # *************  5 Question ****************************



        # *************  6 Question ****************************



     # *************  7 Question ****************************
     #    self.csur.nextQuest()
     #    self.csur.setQuestion("List the features you like most.")
     #
     #    self.csur.SaveQuesAns()

           # *************  8 Question ****************************

        # self.csur.nextQuest()
        # self.csur.setQuestion("Rate our features. (Matrix Rating Scale)")
        #
        # self.csur.SaveQuesAns()


    # *************  9 Question ****************************



        # *************  10 Question ****************************

















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
