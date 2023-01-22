import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from companylist import companyArray

data = {'Company': [], 'LTP': [], 'EPS': [], 'P/E ratio': []}
df = pd.DataFrame(data)

for companyName in companyArray:
    # print("https://merolagani.com/CompanyDetail.aspx?symbol="+companyName)
    url = "https://merolagani.com/CompanyDetail.aspx?symbol="+companyName

    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent, 'html.parser')

    company = companyName

    datatext = soup.find_all("td")

    ltp = datatext[2].text.strip()
    eps = datatext[9].text.strip()
    pe = datatext[10].text.strip()

    # to reomve \r\n    in between eps value and fiscal year
    eps = re.sub(
        r'\r\n                                ', '', eps)

    # print(df)
    # df['Company'] = [title]
    # df['LPT'] = [ltp]
    # df['EPS'] = [eps]
    # df['P/E ratio'] = [pe]
    # df = df.append({'Company': title, 'LPT': ltp, 'EPS': eps,
    #                'P/E ratio': pe}, ignore_index=True)
    # print(len(df))
    df.loc[len(df)] = [company, ltp, eps, pe]

    df.to_json('data.json')
print(df)
