import sys
from core import ImageWrapper
	
if __name__ == "__main__":
	params = {
		"keyword": sys.argv[0],
		"URLNumber": int(sys.argv[1])
	}

	printer = lambda urls: for url in urls: print(url)
	printer(ImageWrapper.URLFind(params))
