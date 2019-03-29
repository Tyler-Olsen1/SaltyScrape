from urllib.parse import parse_qs, urlparse
import requests
from bs4 import BeautifulSoup, SoupStrainer
import csv
import webbrowser
import urllib3

with open('../ExtractedNumbers.csv', 'r') as serials:
    fieldnames = ['Serial_Number', 'Owner']
    try:
        for Serial_Number, line in enumerate(serials, i):
            response = urllib3.urlretrieve(line, "http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=" + str(Serial_Number))
    except: 
        pass
serials.close()
print('Done')

only_td_tags = SoupStrainer("td")
soup = BeautifulSoup(response.text, "html.parser", parse_only=only_td_tags)
targetCell = soup.find(text="Mailing Address:")
print (targetCell.parent.parent.text)