import sys
from core import ImageWrapper
from driverHandler import webdriver_executable
	
if __name__ == "__main__":
	params = {
		"keyword": None,
		"URLNumber": None
	}

	if len(sys.argv) == 1:
		params["keyword"] = input("Enter your keyword:")
		params["URLNumber"] = int(input("Enter the number of images:"))
	else: 
		params["keyword"] = sys.argv[1]
		params["URLNumber"] = int(sys.argv[2])
	
	
	for url in ImageWrapper().URLFind(params):
		print("[URL]: " + url)
