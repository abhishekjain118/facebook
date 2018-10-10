from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import getpass

class FacebookLogin():

    def setUp(self, driver):
        url_fb = "https://en-gb.facebook.com/"
        driver.get(url_fb)

    def login(self, driver):
        fb_username = input("Enter your Facebook username: ")  #user need to input his username
        password = input("Enter your Facebook password: ") #user need to input his password
        fb_password = password
        emailFieldName="email"
        passwordFieldName="pass"
        loginButtonXpath = '//input[@value="Log In"]'

        email_elem = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailFieldName))
        password_elem = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passwordFieldName))
        login_button_elem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        email_elem.clear()
        email_elem.send_keys(fb_username)
        password_elem.clear()
        password_elem.send_keys(fb_password)
        print("Logging in Now ... ")
        login_button_elem.click()

    def logout(self, driver):
        account_settings_elem = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id("userNavigationLabel"))
        account_settings_elem.click()

        logoutXpath = '//span[contains(text(),"Log Out")]'
        logout_elem = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(logoutXpath))
        print("Logging Out Now ... ")
        logout_elem.click()

    def tearDown(self, driver):
        driver.quit()

    def openMarketPlace(self, driver):
        searchXpath = '//input[@name="q"]'
        searchString = "facebook marketplace"
        searchButtonXpath = '//button[@value="1"]'

        search_elem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(searchXpath))
        search_elem.clear()
        search_elem.send_keys(searchString)
        search_button_elem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
            searchButtonXpath))
        search_button_elem.click()

        #marketPlaceXpath = '//a[contains(text(),"facebook marketplace community")]'
        marketPlaceXpath = '//a[contains(@href,"https://www.facebook.com/fbmarketplace")]'
        marketPlace_elem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
            marketPlaceXpath))
        print("Opening Market Place Now ... ")
        marketPlace_elem.click()

    def openLearnMore(self, driver):
        learnMoreButtonXpath = '//button[contains(text(), "Learn More")]'
        learnMore_button_elem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(
            learnMoreButtonXpath))
        print("Learn More ... ")
        learnMore_button_elem.click()

    def searchCars(self, driver, searchParams):
        print("Searching Cars Now ... ")
        searchXpath = '//input[@class="_58al"]'
        search_elems = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath(searchXpath))
        #print(searchParams) #"nissan qashqai", 15000, 5000,
        del search_elems[2] # remove Location and fb search from min, max, location, marketplace_search and fb search
        del search_elems[3] #remove fb search
        search_elems.reverse() #reverse because search_elems are in the order: min, max, marketplace_search
        #print(search_elems)
        for i in range(0, len(search_elems)):
            search_elems[i].clear()
            search_elems[i].send_keys(searchParams[i])
            search_elems[i].send_keys(Keys.RETURN)

    def listOfAllResults(self, driver):
        print("Scraping all results in a list ... ")
        resultXpath = '//a[@class="_1oem"]'
        result_elems = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath(resultXpath))
        return result_elems

    def gatherDataFromResult(self, driver, result):
        print("checking individual results ... ") #TBD

    def main(self): #this main function is for running this script standalone. Otherwise other scripts can import this one and
        #and use all setup, login, logout and teardown etc functions.
        _browser_profile = webdriver.FirefoxProfile() #this section will disable the Notifications from facebook.
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=_browser_profile)
        self.setUp(self.driver)
        self.login(self.driver)
        self.logout(self.driver)
        self.tearDown(self.driver)

if __name__ == "__main__":
    new = FacebookLogin()
    new.main()
