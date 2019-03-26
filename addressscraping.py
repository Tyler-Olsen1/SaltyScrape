import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import writer


URL = 'http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=10040014003'
response = requests.get(URL)

only_strong_tags = SoupStrainer("strong")
soup = BeautifulSoup(response.text, "html.parser", parse_only=only_strong_tags)
# print(soup.prettify())



targetCell = soup.find(text="Mailing Address:")
print (targetCell)



#BODY > tabe > tr > td > table > tr > td> table > tr : 7
