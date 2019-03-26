import requests
from bs4 import BeautifulSoup
import pandas from pandas

res = requests.get("http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=10040014003")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]

print(df[0].to_json(orient='records'))
