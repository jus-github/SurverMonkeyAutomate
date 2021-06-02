from selenium import webdriver

class Login():
    nav_login_xpath = "//div[@id ='root']//div[@class = 'sm-header--anon__addon-default']/a[1]"
    textbox_username_id = "username"
    textbox_password_id="password"
    button_login_xpath="//form[@id = 'sign_in_form']//button[text() = 'LOG IN']"

    def __init__(self , driver):
        self.driver = driver

    def nav_click(self):
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_link_text('Login')
        self.driver.find_element_by_xpath(self.nav_login_xpath).click()

    def setUserName(self , username):
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self , password):
        # self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()