from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fb_login_logout import FacebookLogin

class FacebookMarketSearch():



    def main(self):
        searchString = "nissan qashqai" #change this
        max_value = 15000 #change this
        min_value = 5000  # change this
        searchParams = [searchString, max_value, min_value]

        _browser_profile = webdriver.FirefoxProfile()  # this section will disable the Notifications from facebook.
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=_browser_profile)
        print("this is main")

        fb_login = FacebookLogin()
        fb_login.setUp(self.driver)
        fb_login.login(self.driver)
        fb_login.openMarketPlace(self.driver)

        time.sleep(5)
        #windows_before = self.driver.current_window_handle
        #print("first window handle is: "+ windows_before)
        fb_login.openLearnMore(self.driver)

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window) #driver switched to new window. Learn More button opens new window
        time.sleep(15) #New window takes time to load
        #print("page title after switching is:" + self.driver.title)
        #print("second window handle is: " + new_window)

        fb_login.searchCars(self.driver,searchParams)
        time.sleep(2)
        listOfAllResults = fb_login.listOfAllResults(self.driver)
        #print(len(listOfAllResults), listOfAllResults)

        time.sleep(1)
        for result in listOfAllResults:
            fb_login.gatherDataFromResult(self.driver, result)

        if False:
            time.sleep(5)
            fb_login.logout(self.driver)
            fb_login.tearDown(self.driver)

if __name__ == "__main__":
    new = FacebookMarketSearch()
    new.main()
