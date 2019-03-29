import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import reader
import csv
import urllib

with open("../ExtractedNumbers.csv", newline='') as csvfile:
    ExtractedNumbers = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in ExtractedNumbers:
        str(row)
        # print(row[1:9])
        # print(row[0])

serialnumber=row[1:9]

args = {"av_serial": serialnumber}
# url = "http://127.0.0.1:5000/data?{}".format(urllib.urlencode(args))
URL = "http://www.utahcounty.gov/LandRecords/Property.asp?{}".format(urllib.parse.urlencode(args))
response = requests.get(URL)
print(response)
print(URL)

only_td_tags = SoupStrainer("td")
soup = BeautifulSoup(response.text, "html.parser", parse_only=only_td_tags)
targetCell = soup.find(text="Mailing Address:")
# print (targetCell.parent.parent.text)
