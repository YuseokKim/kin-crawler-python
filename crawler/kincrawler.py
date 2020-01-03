import time

import pyperclip
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]




class KinCrawler(metaclass=Singleton):
    def __init__(self):
        self.driver =  None

    def create_driver(self, driver_location):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('disable-gpu') #GPU 사용 x
        self.options.add_argument('window-size=1920x1080') #실제 크롬 창 사이즈
        self.options.add_argument('lang=ko_KR')
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36')
        # self.options.add_argument("user-data-dir=\\user-data\\naver\\")

        self.driver = webdriver.Chrome(driver_location, options=self.options)

        #self.driver.get('about:blank')
        self.driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});") #플러그인 개수 속이기

    def is_driver_daed(self):
        try:
            print(self.driver.title) # title 조회 시 Exception 발생하면 driver 존재 x
            return False
        except:
            return True

    def check_alert_and_go(self, url):
        self.driver.get(url)
        try:
            WebDriverWait(self.driver, 2).until(EC.alert_is_present(),
                                           'Timed out waiting for PA creation ' +
                                           'confirmation popup to appear.')
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            return

    def set_url(self, url):
        self.driver.get(url)

    def finish(self):
        self.driver.quit()

    def show_driver_info(self):
        user_agent = self.driver.find_element_by_css_selector('#user-agent').text
        plugins_length = self.driver.find_element_by_css_selector('#plugins-length').text

    def focus_frame(self, explicit_wait_time, element):
        WebDriverWait(self.driver, explicit_wait_time).until(expected_conditions.frame_to_be_available_and_switch_to_it(element))

    def get_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def get_elements(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def input_by_clipboad(self, xpath, user_input):
        pyperclip.copy(user_input)
        self.driver.find_element_by_xpath(xpath).click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    def input_by_send_key(self, xpath, user_input):
        self.driver.find_element_by_xpath(xpath).send_keys(user_input)

    def click_tag(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def get_element_by_class_name(self, xpath):
        return self.driver.find_element_by_class_name(xpath)

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
