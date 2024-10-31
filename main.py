import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class WebAutomation:
    def __init__(self):
        # Define driver, options and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # set dir for downloads
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        """ Automatic login to webpage account """
        # Get webpage
        self.driver.get("https://demoqa.com/login")

        # Locate username, password, and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Send input to fields and click login
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Execute JS to stop add interception
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        """ Automatic form fill in """
        # Locate the 'Elements' dropdown and 'Text Box' and click both
        elements = (WebDriverWait(self.driver, 10).
                    until(EC.visibility_of_element_located((By.XPATH,
                                                            '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        elements.click()

        text_box = self.driver.find_element(By.ID, 'item-0')
        self.driver.execute_script("arguments[0].click();", text_box)

        # Locate the form fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Send input to form fields and submit
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        """ Automatic download of content from webpage """
        # Locate the 'Upload and Download' section and the 'Download' button
        upload_download = (WebDriverWait(self.driver, 10).
                           until(EC.visibility_of_element_located((By.ID, 'item-7'))))
        upload_download.click()

        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)


    def close(self):
        """ Close Browser automation session"""
        # sleep to allow download
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
        webautomation = WebAutomation()
        webautomation.login(username="UserName", password="Pythoncouse1!")
        webautomation.fill_form(fullname="John Doe", email="john@gmail.com",
                                current_address="1 john house, Texas, USA", permanent_address="1 john house, Texas, USA")
        webautomation.download()
        webautomation.close()

