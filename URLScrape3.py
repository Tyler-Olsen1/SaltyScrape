import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import reader
import csv
import urllib
import ast
import numpy as np
import asyncio


with open("../SerialNumbers.csv", newline='') as csvfile:
    SerialNumbers = csv.reader(csvfile)
    for row in SerialNumbers:
        array = np.array(row)
        # print(array)

for i in range(SerialNumbers):
    [float(i) for i in SerialNumbers]
    SerialNumbers[i] = int(SerialNumbers[i])
args = {"av_serial": i}

# def arrayArgs():
#     print(args)

def literal_eval_to_array(SerialNumbers):
    return np.array(ast.literal_eval(SerialNumbers))

# async def arrayI():
#     await arrayArgs() 

def response():
    requests.get(URL)
    print(URL)

async def URL():
    URL = "http://www.utahcounty.gov/LandRecords/Property.asp?{}".format(urllib.parse.urlencode(args))
    await response()
    #     requests.get(URL)
    # print(URL)
    print(response)
    only_td_tags = SoupStrainer("td")
    soup = BeautifulSoup(response().text, "html.parser", parse_only=only_td_tags)
    targetCell = soup.find(text="Mailing Address:")
    print (targetCell.parent.parent.text)
