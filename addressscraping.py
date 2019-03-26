import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import writer

URL = 'http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=10040014003'
response = requests.get(URL)

only_td_tags = SoupStrainer("td")
soup = BeautifulSoup(response.text, "html.parser", parse_only=only_td_tags)

targetCell = soup.find(text="Mailing Address:")
print (targetCell.parent.parent.text)




