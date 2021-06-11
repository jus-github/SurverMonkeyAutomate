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
    survey_name_id = "surveyTitle"
    surveyCat_xpath="/html/body/div[1]/div[2]/div/div[3]/div/div[3]/section/div/div/div/div[2]/div/select"
    create_survey_button_id = "newSurvey"
    logo_xpath ="//div[@id='suggested-design-dialog']/div//a[2]"
    lnk_add_page_title_xpath = "//span[@class='page-title user-generated empty wds-button wds-button--ghost-filled wds-button--sm']"
    page_title_id = 'pageTitle'
    page_desc_id ="pageSubtitle"
    save_page_desc_xpath = "//form[@id='pageTitleForm']/div[2]/a[2]"
    add_ques_xpath = "//div[@id='editTitle']"
    ans_icon_xpath = "//a[@id='changeQType']/span[2]"
    select_Xpath ="//li[@class='add-q-menu-container']//div/a/span[contains(text() , '//a[@data-action = 'DateTimeQuestion']' )]"
    date_xpath="//*[@id='create']/ul/li/ul[2]/li[6]/div/a"
    save_and_next_xpath ="div[@class ='editor-buttons']//a[contains(@class , 'save')]"
    # save_and_next_xpath ="//div[@id='editQuestion']/section[2]/div[3]/div/div/a[1]"
    # next_ques_xpath = "//form[@name='surveyForm']//span/a[1]"
    next_ques_xpath ="//span[@class ='wds-button-group add-question-button-group']/a[1]"
    radio_xpath ="//td[@class='choiceText']/div[@class='rteToolbarContainer empty']"
    radio_select_id ="answerBankCategorySelect"

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
        l=WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, self.add_ques_xpath)))

        # l=self.driver.find_element_by_xpath(self.add_ques_xpath)
        self.driver.execute_script("window.scrollBy(0,500)" ,"")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", l)
        l.send_keys(question)

    def chooseAnswerType(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@id='changeQType']/span[2]"))).click()

        print("Clicked ... .. ")

    def selectAnswer(self):
        self.driver.find_element_by_xpath(self.select_Xpath).click()
        self.driver.execute_script("window.scrollBy(0,500)", "")

    def SaveQuesAns(self):

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class ='editor-buttons']//a[contains(@class , 'save')]"))).click()
        print(" QUESTION ADDED .....!!!!!!!!")
        time.sleep(5)



    def nextQuest(self):
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, self.next_ques_xpath))).click()

        # self.driver.find_element_by_xpath(self.next_ques_xpath).click()
        time.sleep(3)
        print("NEXT QUESTION CLICK ...!!!!")


    def checkbox_value(self,value1 , value2 ,value3, value4 , value5):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             "//td[@class='choiceText']/div[@class='rteToolbarContainer empty']/span")))
        element.click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='rte input mce-content-body mce-edit-focus']"))).send_keys(value1)
        time.sleep(5)

        # self.driver.execute_script("window.scrollBy(0,500)", "")
        #     #  *****************************  2 checkbox ***************************************
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//td[@class='choiceText']/div[@class='rteToolbarContainer empty']/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='rte input mce-content-body mce-edit-focus']"))).send_keys(value2)
        #
        # #  *****************************  3 checkbox ***************************************
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody[@class ='answerSetting singleLine']/tr[6]/td[2]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[6]/td[2]/div/div[1]"))).send_keys(value3)

        time.sleep(4)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody[@class ='answerSetting singleLine']/tr[7]/td[2]/div/span")))
        element.click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[7]/td[2]/div/div[1]"))).send_keys(value4)
        time.sleep(5)


        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody[@class ='answerSetting singleLine']/tr[8]/td[2]/div/span")))
        element.click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[8]/td[2]/div/div[1]"))).send_keys(value5)

        time.sleep(3)


    def multiple_text_box(self, value1 , value2):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody/tr[3]/td[1]/div/span")))
        element.click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody[@class='answerSettingTextboxes']/tr[3]/td[1]/div/div[1]"))).send_keys(value1)
        time.sleep(5)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody/tr[4]/td[1]/div/span")))
        element.click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody[@class='answerSettingTextboxes']/tr[4]/td[1]/div/div[1]"))).send_keys(value2)
        time.sleep(5)
        # self.driver.find_element_by_xpath("//tbody[@class='answerSettingTextboxes']/tr[3]/td[1]/div/div[1]").click()


    def multiple_radio_value(self , value1 , value2 , value3):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody/tr[4]/td[2]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[4]/td[2]/div/div[1]"))).send_keys(value1)

        time.sleep(4)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody/tr[5]/td[2]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[5]/td[2]/div/div[1]"))).send_keys(value2)

        time.sleep(4)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody/tr[6]/td[2]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[6]/td[2]/div/div[1]"))).send_keys(value3)

        time.sleep(4)


    def radio_value(self , value):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//td[@class='choiceText']/div[@class='rteToolbarContainer empty']/span")))
        element.click()
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='rte input mce-content-body mce-edit-focus']"))).send_keys(value)
        self.driver.execute_script("window.scrollBy(0,500)", "")

        time.sleep(3)
        # element.send_keys(value)
        # print("COME ..!")
        # self.driver.implicitly_wait(10)
        # WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
        #     (By.XPATH, "//td[@class='choiceText']/div[@class='rteToolbarContainer empty']/span"))).send_keys(value)
        # print(" QUESTION ADDED .....!!!!!!!!")

    def select_Date(self):
        self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_xpath("//a[@id='changeQType']/span[2]")
        self.driver.execute_script("arguments[0].click();", button)
        # WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
        #     (By.XPATH, self.ans_icon_xpath))).click()

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='create']/ul/li/ul[2]/li[7]/div/a"))).click()
        print("  ADDED .....!!!!!!!!")
        self.driver.execute_script("window.scrollBy(0,500)", "")


    def matrix(self , value1 , value2,value3 ,value4,value5,value6,value7):

        # SERVICE
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody[@class='answerSettingMatrix singleLine']/tr[3]/td[1]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody[@class='answerSettingMatrix singleLine']/tr[3]/td[1]/div/div[1]"))).send_keys(value1)

        time.sleep(4)

        # SUPPORT

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody[@class='answerSettingMatrix singleLine']/tr[4]/td[1]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody[@class='answerSettingMatrix singleLine']/tr[4]/td[1]/div/div[1]"))).send_keys(value2)

        time.sleep(4)

        # RESPONSIVENESS ...

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//tbody[@class='answerSettingMatrix singleLine']/tr[5]/td[1]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody[@class='answerSettingMatrix singleLine']/tr[5]/td[1]/div/div[1]"))).send_keys(value3)

        time.sleep(4)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//*[@id='columnsWrap']/div/table/tbody/tr[2]/td[1]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[2]/td[1]/div/div[@class='rte input mce-content-body mce-edit-focus']"))).send_keys(value4)

        time.sleep(4)
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//*[@id='columnsWrap']/div/table/tbody/tr[3]/td[1]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[3]/td[1]/div/div[@class='rte input mce-content-body mce-edit-focus']"))).send_keys(
            value5)

        time.sleep(4)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//*[@id='columnsWrap']/div/table/tbody/tr[4]/td[1]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[4]/td[1]/div/div[@class='rte input mce-content-body mce-edit-focus']"))).send_keys(
            value6)

        time.sleep(4)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//*[@id='columnsWrap']/div/table/tbody/tr[5]/td[1]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[5]/td[1]/div/div[@class='rte input mce-content-body mce-edit-focus']"))).send_keys(
            value7)

        time.sleep(4)



    def dropdown(self , value1 , value2):
        self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_xpath("//a[@id='changeQType']/span[2]")
        self.driver.execute_script("arguments[0].click();", button)

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='create']/ul/li/ul[2]/li[1]/div/a"))).click()

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//*[@id='rows']/tbody/tr[4]/td[2]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[4]/td[2]/div/div[1]"))).send_keys(
            value1)

        time.sleep(4)

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                         "//*[@id='rows']/tbody/tr[5]/td[2]/div/span")))
        element.click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, "//tbody/tr[5]/td[2]/div/div[1]"))).send_keys(
            value2)

        time.sleep(4)