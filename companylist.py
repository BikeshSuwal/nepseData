import requests
from bs4 import BeautifulSoup

url = "https://merolagani.com/CompanyList.aspx"

companyListHtml = requests.get(url).content
soup = BeautifulSoup(companyListHtml, 'html.parser')
sectorId = int(input(
    "Capital=1   Commercial Banks=2    Corporate Debenture=3   Development Bank=4 Finance=5   Government Bond=6 Hotels And Tourism=7  Hydro Power=8 Investment=9  Life Insurance=10  Manufacturing And Processing=11    Microfinance=12    Mutual Fund=13 Non-Life Insurance=14  Others=15 \n Enter sector number:"))-1
collapseId = "#collapse_"+str(sectorId)
sectorName = ""
if sectorId == 0:
    sectorName = 'Capital'
elif sectorId == 1:
    sectorName = 'CommercialBanks'
elif sectorId == 2:
    sectorName = 'CorporateDebenture'
elif sectorId == 3:
    sectorName = 'DevelopmentBank'
elif sectorId == 4:
    sectorName = 'Finance'
elif sectorId == 5:
    sectorName = 'GovernmentBond'
elif sectorId == 6:
    sectorName = 'HotelsAndTourism'
elif sectorId == 7:
    sectorName = 'HydroPower'
elif sectorId == 8:
    sectorName = 'Investment'
elif sectorId == 9:
    sectorName = 'LifeInsurance'
elif sectorId == 10:
    sectorName = 'ManufacturingAndProcessing'
elif sectorId == 11:
    sectorName = 'Microfinance'
elif sectorId == 12:
    sectorName = 'Mutual Fund'
elif sectorId == 13:
    sectorName = 'Non-LifeInsurance'
elif sectorId == 14:
    sectorName = 'CommercialBanks'
elif sectorId == 15:
    sectorName = 'Others'
companyList = soup.select(collapseId + " td a")
# print(companyList)
companyArray = []
for companytag in companyList:
    companyName = companytag.string
    # print(companyName)
    companyArray.append(companyName)

print(companyArray)
