from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os
import time

import driverHandler

"""
	This class is a singleton class
"""
class ImageWrapper(object):
	
	__instance = None

	__driver = None
	__maxMissed = 10

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
					cls.__driver = webdriver.Chrome(driverPath, chrome_options=options)
					cls.__driver.get("https://www.google.com")
					break
				except:
					# patch chromedriver if not available or updated
					try:
						__driver
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

		# Next thing is scary as fuck
		url =  "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947"%(params["keyword"])
		numberOfImages = params["URLNumber"]
		keyword = params["keyword"]

		print("[INFO] Gathering imagae links")
		
		count = 0
		missed = 0

		urls = list()
		ImageWrapper.__driver.get(url)
		time.sleep(3)
		indx = 1

		while count < numberOfImages:
			try:
				#find and click image
				xPathUrl = '//*[@id="islrg"]/div[1]/div[%s]'%(str(indx))
				imgElement = ImageWrapper.__driver.find_element(By.XPATH, xPathUrl)

				ImageWrapper.__driver.find_element(By.XPATH, xPathUrl).click()

				time.sleep(1)
				xPathFinal = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img'
				imgFinal = ImageWrapper.__driver.find_element(By.XPATH, xPathFinal)
				urlFinal = imgFinal.get_attribute("src")
				urls.append(urlFinal)
				missed = 0
				count += 1
			except Exception:
				missed = missed + 1
				if (missed > ImageWrapper.__maxMissed):
					print("[INFO] Maximum missed photos reached, exiting...")
					break
			indx += 1
		
		ImageWrapper.__driver.quit()
		print("[INFO] Search ended\n")

		return urls
