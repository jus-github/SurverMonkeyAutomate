import time
from selenium.webdriver.support.ui import Select

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
    lnk_add_page_title_xpath = "//div[@id='pageid-167816053']//span[@class='page-title user-generated empty wds-button wds-button--ghost-filled wds-button--sm']"
    page_desc_id ="pageSubtitle"
    save_page_desc_xpath = "//form[@id='pageTitleForm']/div[2]/a[2]"
    add_ques_xpath = "//div[@id=questionTitleWrap']//span[contains(text() , 'Enter your question')]"
    ans_icon_xpath = "//a[@id='changeQType']/span[2]"
    select_Xpath ="//li[@class='add-q-menu-container']//div/a/span[contains(text() , 'Single Textbox' )]"
    save_ques_ans_xpath ="//div[@id='editQuestion']/section[2]/div[3]//a[2]"


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