import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common import exceptions

class Create:
    lnkcreatesrvey_xpath="//div[@id='hd']//a[@class='create-survey alt btn SL_split']"
    # btn_start_xpath ="//button[text() = 'Start from scratch']"
    start_scratch_xpath ="//div[@id='reactApp']//button[contains(text(),'Start from scratch')]"
    # btn_start_xpath = "/html/body/div[1]/div[2]/div/div/div[1]/div[2]/button[1]"
    # start_survey_scratch = "//div[@id = 'reactApp']//h3/strong[text()='Start from scratch']"
    survey_name_id = "surveyTitle"
    surveyCat_xpath="/html/body/div[1]/div[2]/div/div[3]/div/div[3]/section/div/div/div/div[2]/div/select"
    # surveyCat_xpath ="//div[@class='wds-select wds-select--stretched wds-select--md sm-new-survey-modal--select']"
    # drp = Select(surveyCat_id)
    # drp.select_by_value('2')
    create_survey_button_id = "newSurvey"
    logo_xpath ="//div[@id='suggested-design-dialog']/div//a[2]"
    lnk_add_page_title_xpath = "//span[@class='page-title user-generated empty wds-button wds-button--ghost-filled wds-button--sm']"
    page_title_id = 'pageTitle'
    page_desc_id ="pageSubtitle"
    save_page_desc_xpath = "//form[@id='pageTitleForm']/div[2]/a[2]"
    add_ques_xpath = "//div[@id='editTitle']"
    # ans_icon_xpath = "//a[@id='changeQType']/span[2]"
    # select_Xpath ="//li[@class='add-q-menu-container']//div/a/span[contains(text() , 'Single Textbox' )]"
    save_ques_ans_xpath ="//div[@id='editQuestion']/section[2]/div[3]//a[2]"
    next_ques_xpath = "//form[@name='surveyForm']//span/a[1]"
    radio_xpath ="//table[@id='rows']/tbody/tr[4]/td[2]/div/span"

    def __init__(self , driver):
        self.driver = driver

    def clickOnCreateSurvey(self):
        self.driver.find_element_by_xpath(self.lnkcreatesrvey_xpath).click()

    def clickOnStartFromScratch(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.start_scratch_xpath).click()

    def setSurveyName(self , surveyname):
        self.driver.find_element_by_id(self.survey_name_id).send_keys(surveyname)

    def setSurveyCategory(self):
        element = self.driver.find_element_by_xpath(self.surveyCat_xpath)
        self.driver.implicitly_wait(10)
        drp = Select(element)
        drp.select_by_visible_text('Customer feedback')
        print("select customer feed back ....!")

    def clickOnCreate(self):
        self.driver.find_element_by_id(self.create_survey_button_id).click()

    def AddPageTitle(self):
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_xpath(self.lnk_add_page_title_xpath).click()

    def setPageTitle(self , pagetitle):
        self.driver.find_element_by_id(self.page_title_id).send_keys(pagetitle)

    def setPageDesc(self , pagedesc):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id(self.page_desc_id).send_keys(pagedesc)

    def savePageTitle(self):
        self.driver.find_element_by_xpath(self.save_page_desc_xpath).click()
        print("Title Saved .....!!!!!!!!!!!")

    def setQuestion(self , question):
        self.driver.implicitly_wait(10)
        l=self.driver.find_element_by_xpath(self.add_ques_xpath)
        self.driver.execute_script("window.scrollBy(0,500)" ,"")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", l)
        l.send_keys(question)

    def chooseAnswerType(self):
        self.driver.find_element_by_xpath(self.ans_icon_xpath).click()

    def selectAnswer(self):
        self.driver.find_element_by_xpath(self.select_Xpath).click()

    def SaveQuesAns(self):
        l=self.driver.find_element_by_xpath(self.save_ques_ans_xpath)
        # l.click()
        try:
            l.click()
        except exceptions.StaleElementReferenceException as e:
            print(e)

        time.sleep(10)
    def nextQuest(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.next_ques_xpath).click()

    def radio_value(self , value):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.radio_xpath).send_keys(value)