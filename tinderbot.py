from selenium import webdriver
from time import sleep


class Tinder():

    def __init__(self):
        self.driver = webdriver.Chrome('C:\chromedriver')

    def login(self):
        self.driver.get("https://tinder.com/")
        sleep(1)
        fb = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button') 
        fb.click()

        sleep(1)
        fb_login = self.driver.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[1]/div/div[3]/span/div[2]/button")
        sleep(1)
        fb_login.click()
        okno1 = self.driver.window_handles[0]
        self.driver.switch_to_window(bot.driver.window_handles[1])

        sleep(1)

        email = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        email.send_keys('mail@mail.com')

        pw = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')  
        pw.send_keys('Password')

        loginbt = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]')
        loginbt.click()

        self.driver.switch_to_window(okno1)
    def zamknij(self):
            sleep(1)
            location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            location.click()
            sleep(1)
            notification = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
            notification.click()
            sleep(1)



    def lubie(self):
    
            sleep(1)
            like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

            like.click()


    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def close_popup(self):
        popup3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup3.click()


    def auto(self):
        while True:
            sleep(1)
            try:
                self.lubie()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

            self.lubie()
