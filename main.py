from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PROMISED_DOWN = 200 #Enter the promised download speed by your ISP
PROMISED_UP = 20 #Enter the promised upload speed by your ISP
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH" # e.g. "C:/Development/chromedriver.exe"
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASSWORD = "YOUR PASSWORD"
TWITTER_USERNAME = "YOUR TWITTER USERNAME"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = ChromeService(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=option)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
     self.driver.get('https://fast.com/')
     sleep(30)
     
     show_more_info_button = self.driver.find_element(by = By.ID, value = 'show-more-details-link')
     show_more_info_button.click()

     self.down = int(self.driver.find_element(by=By.ID, value = 'speed-value').text)
     print(f"The Download Speed is: {self.down} Mbps.")

     self.up = int(self.driver.find_element(by=By.ID, value = 'upload-value').text)
     print(f"The Upload Speed is: {self.up} Mbps.")
     # print(down_speed)
        
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home')
        
        sleep(5)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        sleep(5)
        try:
            password_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys(TWITTER_USERNAME)
            username.send_keys(Keys.ENTER)
            sleep(5)
            password_input = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
            
        #Composing tweet for complaint
        sleep(5)
        tweet = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        tweet.send_keys(f"@ViettelGroup, my current Internet Speed is is {self.down} Mbps for Download and {self.up} Mbps for Upload whereas I was promised {PROMISED_DOWN} Mbps Download and {PROMISED_UP} Mbps Upload, fix your service!")
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        tweet_button.click()
        sleep(3)
        print("Tweet Composed.")
        
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()