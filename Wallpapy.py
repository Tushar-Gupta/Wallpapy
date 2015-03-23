
from BeautifulSoup import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys
import ctypes
import win32con
import time

def setWallpaperWithCtypes(path):
    cs = ctypes.c_buffer(path)
    ok = ctypes.windll.user32.SystemParametersInfoA(win32con.SPI_SETDESKWALLPAPER, 0, cs, 0)

def main(url, out_folder="/images/"):
    lastTopImageURL = ""
    ext = ["jpg","jpeg","png","bmp"]
    while True:
        try:
            soup = bs(urlopen(url))
            parsed = list(urlparse.urlparse(url))
            allImages =  soup.findAll('a', {'class': 'title may-blank '})
            topImageURL = allImages[1]['href']
            if  not (topImageURL.endswith(tuple(ext))):
                topImageURL = topImageURL + ".jpg"
            if not (topImageURL == lastTopImageURL):
                lastTopImageURL = topImageURL
                urlretrieve(topImageURL, "images/topImage.jpg")
                setWallpaperWithCtypes(os.path.abspath("images/topImage.jpg"))
        except:
            print "\nToo many requests. Will try again in 2 minutes."    
        time.sleep(120)
    
if __name__ == "__main__":
    url = "http://www.reddit.com/r/EarthPorn/top/"
    out_folder = "/images/"
    main(url, out_folder)
 

    