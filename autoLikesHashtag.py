from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def closeBrowser(self):
        self.bot.close()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(15)
        bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        time.sleep(5)
        bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button').click()
        time.sleep(5)
        bot.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(5)
        
        

    def like_post(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag)
        time.sleep(5)
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
        hrefs = bot.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        for pic_href in pic_hrefs:
            bot.get(pic_href)
            time.sleep(2)
            try:
                bot.find_element_by_class_name('fr66n').click()
                time.sleep(10)
            except Exception as e:
                time.sleep(2)

# Zmień login oraz haslo na prawidlowe.
user = InstagramBot('login', 'haslo')

user.login()

# Wpisz hashtag na wybrany przez Ciebie
user.like_post('polishgirl')


