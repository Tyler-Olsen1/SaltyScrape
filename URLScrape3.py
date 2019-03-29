import requests
from bs4 import BeautifulSoup#, SoupStrainer
from csv import reader
import csv
import urllib
import numpy as np
import pandas as pd
import asyncio


page = requests.get('http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=20160026')

soup = BeautifulSoup(page.text, 'html.parser')
only_td_tags = soup.find("td")
targetCell = soup.find(text="Mailing Address:")
print (targetCell.parent.parent.text)

