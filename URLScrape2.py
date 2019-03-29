import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import reader
import csv
import urllib
import numpy as np

with open("../SerialNumbers.csv", newline='') as csvfile:
    SerialNumbers = csv.reader(csvfile)
    for row in SerialNumbers:
        row = np.array(row)
        print(row)

serialnumber=int(row)
# newSerialNumber=serialnumber[:2]+serialnumber[10:]
# print(newSerialNumber)
args = {"av_serial": serialnumber}
# url = "http://127.0.0.1:5000/data?{}".format(urllib.urlencode(args))
URL = "http://www.utahcounty.gov/LandRecords/Property.asp?{}".format(urllib.parse.urlencode(args))
response = requests.get(URL)
print(URL)
print(response)

only_td_tags = SoupStrainer("td")
soup = BeautifulSoup(response.text, "html.parser", parse_only=only_td_tags)
targetCell = soup.find(text="Mailing Address:")
print (targetCell.parent.parent.text)
