from selenium import webdriver
from time import sleep

class Spammer():
    def __init__(self):
        super().__init__()
        self.wd = webdriver.Chrome()
        #Getting Whatsapp web
        self.wd.get('https://web.whatsapp.com')
        #Making sure it logs out when the browser closes
        keep_log = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/label/input')
        keep_log.click()
        #Press enter when you're in
        input('Enter when log in.')

    def search_chat(self, name):
        self.name = name
        #Selecting the search_bar and typing into it
        search_bar = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        search_bar.click()
        search_bar.send_keys(self.name)
        sleep(1)
        #Clicking on the contact
        chat = self.wd.find_element_by_class_name('_3CneP')
        chat.click()

    def spam_msg(self, msg, times):
        self.times = times
        self.msg = msg
        #Spamming messages
        for times in range(self.times):
            text_box = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
            text_box.send_keys(self.msg)
            send_button = self.wd.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
            send_button.click()
        self.wd.close()

#Assigning the object to a variable       
bot = Spammer()
#Calling the funcions of the object
bot.search_chat('Name of the contact to spam')
bot.spam_msg('Message', 'Number of messages to spam (int type required)')
