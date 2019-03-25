import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import writer

URL = 'http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=10040014003'
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

only_strong_tags = SoupStrainer("strong")

# print(soup)
# these two lines work. I'm experimenting
# for strong_tag in soup.find_all('strong')[3:4]:
#     print strong_tag


# targetCell = soup.find(text="Mailing Address:")
# print (targetCell)



BODY > tabe > tr > td > table > tr > td> table > tr : 7
