import time

from datetime import datetime


from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import *
from selenium.webdriver.chrome.options import Options


# from Utils.Generic_reporting import *

import keyboard

class browser_session ():
    def __init__(self, browser, url):
        if browser == 'chrome':
            chrome_options = Options()
            # managed_default_content_settings.images = 2: Disable images load, this setting can improve pageload & save bandwidth
            # chrome_prefs = {
            #     'profile.managed_default_content_settings.images': 2
            # }
            # chrome_options.add_experimental_option('prefs', chrome_prefs)

            self.browser = webdriver.Chrome('D:\\UserData\z0047pav\Tools\selenium_drivers\chromedriver.exe', chrome_options=chrome_options)
            self.browser.get(url)
        if browser == 'firefox':
            self.browser = webdriver.Firefox(executable_path='C:\Selenium_drivers\geckodriver.exe')
            self.browser.get(url)

    def click_on_element_by_xpath(self, xpath, report_file_stream, timeout=30,lapse=0):
        """
        Clicks on one element defined by xpath of the web-page displayed on a given browser instance


        :param xpath: xpath of the element to be clicked
        :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
        :param timeout: maximum time during which the script will wait for the to be loaded
                after the time out the action will fail
        :return: returns the element
        """
        try:
            element = WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))


            time.sleep(lapse)

            element.click()

        except:

            if (report_file_stream is not None):
                report_file_stream.write(
                    '<font color=#800080>%s</font>: Clicking on the element defined defined by the following XPath "%s": <font color=#FF0000>FAILED</font><br />' % (
                    datetime.now().strftime("%H:%M:%S.%f"), xpath))
                date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
                filename = "failure_screen_shot_%s.png" % date_time_string
                #self.browser.get_screenshot_as_file(filename)
                report_file_stream.write("Screen shot saved on file: %s<br />" % filename)

            return None
        else:
            if (report_file_stream is not None):
                report_file_stream.write(
                    '<font color=#800080>%s</font>: Clicking on the element defined defined by the following XPath "%s": <font color=#00FF00>PASSED</font><br />' % (
                    datetime.now().strftime("%H:%M:%S.%f"), xpath))


            return element

    def send_keys_to_element_by_xpath(self, xpath, keys, report_file_stream, timeout=30):
        """
        Fills text in one form element defined by xpath in the web-page displayed on a given browser instance


        :param xpath: xpath of the element to be filled in
        :param keys: text to be entered in the form element
        :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
        :param timeout: maximum time during which the script will wait for the to be loaded
                after the time out the action will fail
        :return: returns the element

        """

        try:
            element = WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))

            element.clear()

            element.send_keys(keys)

        except:
            if (report_file_stream is not None):
                report_file_stream.write(
                    "<font color=#800080>%s</font>: Sending keys to the element defined defined by the following XPath '%s': <font color=#FF0000>FAILED</font><br />" % (
                    datetime.now().strftime("%H:%M:%S.%f"), xpath))
                date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
                filename = "failure_screen_shot_%s.png" % date_time_string
                self.browser.get_screenshot_as_file(filename)
                report_file_stream.write("Screen shot saved on file: %s<br />" % filename)
            return None
        else:
            if (report_file_stream is not None):
                report_file_stream.write(
                    "<font color=#800080>%s</font>: Sending keys to the element defined defined by the following XPath '%s': <font color=#00FF00>PASSED</font><br />" % (
                    datetime.now().strftime("%H:%M:%S.%f"), xpath))
            return element

    def wait_for_a_given_text_to_be_present (self, text, report_file_stream, timeout = 30):
        """
        waits for the presence of a given text web page to be loaded


        :param text: the text to be detected
        :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
        :param timeout: maximum time during which the script will wait for the to be loaded
            after the time out the action will fail
        :return: True if the text is found before time out
            False otherwise
        """
        try:
            element = WebDriverWait (self.browser,timeout).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[(contains(text(), '%s') or contains(., '%s'))]"%(text,text))))
        except:
            if (report_file_stream is not None):
                report_file_stream.write('<font color=#800080>%s</font>: The following text string ( "%s") was not found within thw timeout window (%s seconds).<font color=#FF0000>FAILED</font><br />' % (datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"), text, timeout))
                date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
                filename = "failure_screen_shot_%s.png" % date_time_string
                self.browser.get_screenshot_as_file(filename)
            #print("Unexpected error:", sys.exc_info())
            if (report_file_stream is not None):
                report_file_stream.write("Screen shot saved on file: %s<br />" % filename)
            return None
        else:
            if (report_file_stream is not None):
                report_file_stream.write('<font color=#800080>%s</font>: The following text string ( "%s") was rendered.<font color=#00FF00>PASSED</font><br />' % (datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f") ,text))
            return element

    def get_text_by_xpath(self, xpath, timeout=30):
        """
        Reads the text contained in a given web element defined by xpath

        :param browser: browser instance where the actions will be performed
        :param xpath:  xpath of the element
        """
        try:
            time.sleep(10)
            element = WebDriverWait(self.browser, timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except:
            date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
            filename = "failure_screen_shot_%s.png" % date_time_string
            self.browser.get_screenshot_as_file(filename)
            return None
        else:
            return element.text

    def enter_date_on_calendar (self, xpath, day, dif_month, report_file_stream):
        """
        Enters the date on the calendar provided the day of the month to be selected.
        And the difference in months between the default date of the calendar and the date to be selected

        For example, if the default date of the calendar is March 2021,
        a) if the date to be scheduled, is on March 2021 dif_month = 0
        b) if the date to be scheduled in on April 2021 dif_month = 13
        c) if the date to be scheduled is on February 2020 dif_month = -13
        """

        self.click_on_element_by_xpath(xpath, report_file_stream)

        next_month_xpath = "//button[@title='Next month']"

        previous_month_xpath = "//button[@title='Previous month']"

        if dif_month > 0:
            relevant_xpath = next_month_xpath
        else:
            relevant_xpath = previous_month_xpath

        dif_month_absolute_value = abs(dif_month)

        for i in range (dif_month_absolute_value):
            self.click_on_element_by_xpath(relevant_xpath,
                                                           report_file_stream)


        self.click_on_element_by_xpath("//*[@class = 'custom-day text-center bb-input-datepicker__single-day' and (text() = ' %s ' or . = ' %s ')]" % (day, day), report_file_stream)

    def select_element_by_xpath_and_text (self, xpath, text, report_file_stream, timeout = 30):
        """
        Selects one option on a drop down menu.
        The drop down menu referred by xpath.
        And the element to be selected is identified by its text.

        :param browser: browser instance created by the selenium webdriver
        :param xpath: xpath of the drop down menu.
        :param text: text of the element to select
        :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
        :param timeout: maximum time during which the script will wait for the to be loaded
            after the time out the action will fail
        :return: returns the element
        """


        try:

            element = WebDriverWait (self.browser,timeout).until(expected_conditions.element_to_be_clickable((By.XPATH,xpath)))

            time.sleep (2)

            Select (element).select_by_visible_text(text)


        except:
            if (report_file_stream is not None):
                report_file_stream.write('<font color=#800080>%s</font>: Selcting "%s" on the element defined defined by the following XPath "%s": <font color=#FF0000>FAILED</font><br />' % (datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"), text, xpath))
                date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
                filename = "failure_screen_shot_%s.png" % date_time_string
                self.browser.get_screenshot_as_file(filename)
            if (report_file_stream is not None):
                report_file_stream.write("Screen shot saved on file: %s<br />" % filename)

        else:
            if (report_file_stream is not None):
                report_file_stream.write('<font color=#800080>%s</font>: Selcting "%s" on the element defined defined by the following XPath "%s": <font color=#00FF00>PASSED</font><br />' % (datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"), text, xpath))
            return element

    def select_element_by_xpath_and_value (self, xpath, value, report_file_stream, timeout = 30):
        """
        Selects one option on a drop down menu.
        The drop down menu referred by xpath.
        And the element to be selected is identified by its value.

        :param browser: browser instance created by the selenium webdriver
        :param xpath: xpath of the drop down menu.
        :param value: value of the element to select
        :param report_file_stream: the file where the result of the action (pass vs fail) will be stored
        :param timeout: maximum time during which the script will wait for the to be loaded
            after the time out the action will fail
        :return: returns the element
        """


        try:
            element = WebDriverWait (self.browser,timeout).until(expected_conditions.presence_of_element_located((By.XPATH,xpath)))

            Select (element).select_by_value (value)

        except:
            if (report_file_stream is not None):
                report_file_stream.write('<font color=#800080>%s</font>: Selecting the element with value %s in the drop down menu defined by the following XPath "%s": <font color=#FF0000>FAILED</font><br />' % (datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"), value, xpath))
                date_time_string = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
                filename = "failure_screen_shot_%s.png" % date_time_string
                self.browser.get_screenshot_as_file(filename)
                report_file_stream.write("Screen shot saved on file: %s<br />" % filename)
            exit(1)
        else:
            if (report_file_stream is not None):
                report_file_stream.write('<font color=#800080>%s</font>: Selecting "the element with value %s in the drop down defined defined by the following XPath "%s": <font color=#00FF00>PASSED</font><br />' % (datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"), value, xpath))
            return element

