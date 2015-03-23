
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
            print "\nChecking again.."
            soup = bs(urlopen(url))
            parsed = list(urlparse.urlparse(url))
            allImages =  soup.findAll('a', {'class': 'title may-blank '})
            topImageURL = allImages[1]['href']
            if  not (topImageURL.endswith(tuple(ext))):
                topImageURL = topImageURL + ".jpg"
            if not (topImageURL == lastTopImageURL):
                print "New top image found.."
                lastTopImageURL = topImageURL
                print "Downloading new image.."
                urlretrieve(topImageURL, "images/topImage.jpg")
                print "Download complete..\nSetting as wallpaper"
                setWallpaperWithCtypes(os.path.abspath("images/topImage.jpg"))
                print "\nNew image set as wallpaper.\nWill check again in a minute."
            else:
                print "Top image is still the same.\nWill check again in a minute."
        except:
            print "\nToo many requests. Will try again in a minute."    
        time.sleep(60)
    
if __name__ == "__main__":
    url = "http://www.reddit.com/r/EarthPorn/top/"
    out_folder = "/images/"
    main(url, out_folder)
 

    