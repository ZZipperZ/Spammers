from selenium import webdriver
from time import sleep

class Spammer():
    def __init__(self):
        super().__init__()
        self.wd = webdriver.Chrome()
        self.wd.get('https://web.whatsapp.com')
        keep_log = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/label/input')
        keep_log.click()
        input('Enter when log in.')

    def search_chat(self, name):
        self.name = name
        search_bar = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        search_bar.click()
        search_bar.send_keys(self.name)
        sleep(1)
        chat = self.wd.find_element_by_class_name('_3CneP')
        chat.click()

    def spam_msg(self, msg, times):
        self.times = times
        self.msg = msg
        for times in range(self.times):
            text_box = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            text_box.send_keys(self.msg)
            send_button = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
            send_button.click()
        self.wd.close()

bot = Spammer()
bot.search_chat('Name of the contact to spam')
bot.spam_msg('Message', 'Number of messages to spam')
