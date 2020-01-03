class Naver(object):

    def __init__(self, user_id, user_pw):
        self.id = user_id
        self.pw = user_pw
        self.login_xpath_in_main_page = '//*[@id="account"]/div/a/i'
        self.id_xpath = '//*[@id="id"]'
        self.pw_xpath = '//*[@id="pw"]'
        self.login_xpath_in_login_page = '//*[@id="frmNIDLogin"]/fieldset/input'
        self.register_xpath = '//*[@id="frmNIDLogin"]/fieldset/span[1]/a'
        self.keep_login_state_xpath = '//*[@id="login_maintain"]/span[1]/a'
        #self.list_xpath_in_kin_question = '//*[@id="s_content"]/div[3]/ul/li[1]/dl/dt/a'
        self.list_xpath_in_kin_question = '//*[@id="au_board_list"]/tr[1]/td[1]/a'
        self.title_xpath_in_kin_question = '//*[@id="content"]/div[1]/div/div[1]/div[2]//*[@class="title"]'
        self.content_xpath_in_kin_question = '//*[@id="content"]/div[1]/div/div[1]/div[3]'
        self.reply_xpath = '//*[@id="answerWriteButton"]'
        self.reply_content_xpath = '//*[@class="se-drop-indicator"]/div/div/p/span'
        self.reply_register_xpath = '//*[@id="answerRegisterButton"]'

    def get_reply_xpath(self):
        return self.reply_xpath

    def get_login_xpath_in_main_page(self):
        return self.login_xpath_in_main_page

    def get_login_xpath_in_login_page(self):
        return self.login_xpath_in_login_page

    def get_register_xpath(self):
        return self.register_xpath

    def get_keep_login_state_xpath(self):
        return self.keep_login_state_xpath

    def get_list_xpath_in_kin_question(self):
        return self.list_xpath_in_kin_question

    def get_content_xpath_in_kin_question(self):
        return self.content_xpath_in_kin_question

    def get_title_xpath_in_kin_question(self):
        return self.title_xpath_in_kin_question

    def get_id_xpath(self):
        return self.id_xpath

    def get_pw_xpath(self):
        return self.pw_xpath

    def get_id(self):
        return self.id

    def get_pw(self):
        return self.pw