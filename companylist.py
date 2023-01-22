import requests
from bs4 import BeautifulSoup

url = "https://merolagani.com/CompanyList.aspx"

companyListHtml = requests.get(url).content
soup = BeautifulSoup(companyListHtml, 'html.parser')

companyList = soup.select("#collapse_11 td a")
# print(companyList.string)
companyArray = []
for companytag in companyList:
    companyName = companytag.string
    # print(companyName)
    companyArray.append(companyName)

# print(companyArray)
