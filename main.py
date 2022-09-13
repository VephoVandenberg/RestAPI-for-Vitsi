import sys
import os
from core import ImageWrapper
from driverHandler import webdriver_executable
	
if __name__ == "__main__":
	params = {
		"keyword": sys.argv[1],
		"URLNumber": int(sys.argv[2])
	}
	
	app_path = os.path.dirname(os.path.realpath(__file__))
	for url in ImageWrapper().URLFind(params):
		print(url)
