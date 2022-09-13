from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

import driverHandler

"""
	This class is a singleton class
"""
class ImageWrapper(object):
	
	__instance = None

	__driverPath = None
	__driver = None
	__searchKey = None
	__numberOfImages = None
	__minResolution = None
	__maxResolution = None

	def __new__(cls, *args, **kwargs):
		if not cls.__instance:
			cls.__instance = super(ImageWrapper, cls).__new__(cls)

			driverPath = os.path.normpath(os.path.join(os.getcwd(), "webdriver", driverHandler.webdriver_executable()))
			# We have to check if chromedriver is updated
			headless = True
			while True:
				try:
					options = Options()
					if headless:
						options.add_argument("--headless")
					driver = webdriver.Chrome(driverPath, chrome_options=options)
					driver.get("https://www.google.com")
					break
				except:
					# patch chromedriver if not available or updated
					try:
						driver
					except NameError:
						is_patched = driverHandler.download_lastest_chromedriver()
					else:
						is_patched = driverHandler.download_lastest_chromedriver(driver.capabilities['version'])
					if not is_patched:
						exit("Update your webdriver")

		return cls.__instance

	def URLFind(self, params) -> list:
		"""
			Method returns a list of urls 
			based on a params dictionary given as an argument
		"""
		return list()
