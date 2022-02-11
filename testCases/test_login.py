import pytest

from selenium import webdriver



# from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info('*******TEST_001_LOGIN*******')
        self.logger.info('******** Verifying Home Page Title******')
        print(self.logger)
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info('******** Home Page title test is passed ********')
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_homePageTitle.png')
            self.driver.close()
            self.logger.error('******** Home Page title is Passes *********')

            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info('*******verifying Login Test*******')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info('*******Verifying Login test*******')
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_login.png')
            self.driver.close()
            self.logger.error('********Login test is failed*******')
            assert False



