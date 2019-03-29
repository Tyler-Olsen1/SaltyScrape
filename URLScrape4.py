import requests
from bs4 import BeautifulSoup#, SoupStrainer
from csv import reader
import csv
import urllib
import numpy as np
import pandas as pd
import asyncio

page = requests.get('http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=20160026')


with open("./SerialNumbers.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        seriallist = row
    serialnumber = [int(i) for i in seriallist(1, 6009)]
    print(serialnumber)
        
    # for serialnumber = [i]reader
    #     print(serialnumber)

# pages = []

# for i in serialnumber(1, 6009):
#     url = 'http://www.utahcounty.gov/LandRecords/Property.asp?av_serial='+ str(i) 
#     pages.append(url)

# soup = BeautifulSoup(page, 'html.parser')
# only_td_tags = soup.find("td")
# targetCell = soup.find(text="Mailing Address:")
# print (targetCell.parent.parent.text)

# #Created a file to write to
# f = csv.writer(open("./URL_Addresses.csv", 'w'))
# f.writerow(['Address'])

# # for i in serialnumber: 
# #     number = 
