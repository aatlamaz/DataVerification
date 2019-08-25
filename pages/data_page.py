from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import time
import utilities

class DatabaseVerification(SeleniumDriver):
    def _init_(self, driver):
        super()._init_(driver)
        self.driver = driver


    ### Locators ###
    _run_sql_button = "//button[@type='button' and @class='w3-green w3-btn']"
    _number_of_records = "//div[contains(text(),'Number of Records: 62')]"
    _code_mirror_lines = "//div[@class='CodeMirror-lines']"


    def typecodemirror(self):
        return self.clearField(self._code_mirror_lines,locatorType="xpath")
    def clickrunsqlbutton(self):
        return self.elementClick(self._run_sql_button,locatorType="xpath")
    def textnumberofrecords(self):
        return self.getText(self._number_of_records,locatorType="xpath")


    ##call

    def codemirrorline(self):
        self.typecodemirror()
    def runsqlbutton(self):
        self.clickrunsqlbutton()
    def texttablenumbers(self):
        self.textnumberofrecords()

