# practice for crawl google photo by the package

from google_images_download import google_images_download  # importing the library

response = google_images_download.googleimagesdownload()  # class instantiation

arguments = {"keywords": "ha", "limit": 10, "print_urls": True}  # creating list of arguments
paths = response.download(arguments)  # passing the arguments to the function
print(paths)  # printing absolute paths of the downloaded images

#########################################################################

# importing google_images_download module
from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

search_queries = ['milk']
# ['The smartphone also features an in display fingerprint sensor.',    'The pop up selfie camera is placed aligning with the rear cameras.',    '''In terms of storage Vivo V15 Pro could offer        up to 6GB of RAM and 128GB of onboard storage.''',    'The smartphone could be fuelled by a 3 700mAh battery.',]


def downloadimages(query):
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query,
                 # "format": "jpg",
                 # "limit": 40,
                 # "print_urls": True,
                 # "size": "medium",
                 # "aspect_ratio": "panoramic"
                }
    try:
        response.download(arguments)

        # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": query,
                     "format": "jpg",
                     "limit": 100,
                     "print_urls": True,
                     "size": "medium"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass


# Driver Code
for query in search_queries:
    downloadimages(query)
    print()

############################################

from bs4 import BeautifulSoup
import requests
import re
# import urllib2
import urllib3
import os
import cookielib
import json


def get_soup(url, header):
    return BeautifulSoup(urllib3.urlopen(urllib2.Request(url, headers=header)), 'html.parser')


# query = raw_input("query image")  # you can change the query for the image  here
query = raw_input("milk")  # you can change the query for the image  here
image_type = "ActiOn"
query = query.split()
query = '+'.join(query)
url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
print(url)
# add the directory for your image here
DIR = "Pictures"
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url, header)

ActualImages = []  # contains the link for Large original images, type of  image
for a in soup.find_all("div", {"class": "rg_meta"}):
    link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    ActualImages.append((link, Type))

print("there are total", len(ActualImages), "images")

if not os.path.exists(DIR):
    os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
    os.mkdir(DIR)
###print images
for i, (img, Type) in enumerate(ActualImages):
    try:
        req = urllib2.Request(img, headers={'User-Agent': header})
        raw_img = urllib2.urlopen(req).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print(cntr)
        if len(Type) == 0:
            f = open(os.path.join(DIR, image_type + "_" + str(cntr) + ".jpg"), 'wb')
        else:
            f = open(os.path.join(DIR, image_type + "_" + str(cntr) + "." + Type), 'wb')

        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : " + img)
        print(e)
