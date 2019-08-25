from selenium import webdriver
from pages.data_page import DatabaseVerification
import time
# import unittest
from base.webdriverfactory import WebDriverFactory

class DataTest():
    def testingdatabase(self):

        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        """TestCase TC001;Click Run SQL button and see table """


        dtb = DatabaseVerification(driver)
        dtb.codemirrorline()
        dtb.runsqlbutton()
        element="//button[@class='w3-green w3-btn']"

        if element.is_enabled():
            print("TestCase TC001 IS PASS")
        else:
            print("TestCase TC001 IS FAIL")

        """TestCase TC002; Get all table numbers"""

        dtb.texttablenumbers()
        expectnumber = "62"

        if expectnumber==dtb.texttablenumbers():
            print("TestCase TC002 IS PASS")
        else:
            print("TestCase TC002 IS FAIL")



dt = DataTest()
dt.testingdatabase()

