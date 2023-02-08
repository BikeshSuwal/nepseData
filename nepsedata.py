import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from companylist import companyArray, sectorName
import tqdm

# Initialize a dictionary to store the data
data = {'Company': [], 'LTP': [], 'EPS': [], 'P/E ratio': []}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

for companyName in tqdm.tqdm(companyArray):
    try:
        # Form the URL for each company
        url = "https://merolagani.com/CompanyDetail.aspx?symbol=" + companyName

        # Send a GET request to the URL
        r = requests.get(url)
        r.raise_for_status()

        # Extract the content of the response
        html_content = r.content

        # Create a BeautifulSoup object from the content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Get the company name
        company = companyName

        # Find all `td` elements in the content
        data_text = soup.find_all("td")

        # Extract the values for LTP, EPS, and P/E ratio
        ltp = data_text[2].text.strip()
        eps = data_text[9].text.strip()
        pe = data_text[10].text.strip()

        # Remove the unwanted characters from the EPS value
        eps = re.sub(r'\r\n                                ', '', eps)

        # Append the values to the DataFrame
        df = df.append({'Company': company, 'LTP': ltp,
                       'EPS': eps, 'P/E ratio': pe}, ignore_index=True)
    except Exception as e:
        print(f"Error while processing company {companyName}: {e}")

# Save the DataFrame as a JSON file
df.to_json(sectorName + '.json', orient='records')

print(df)
input("This data has been stored in "+sectorName +
      ".json file in current directory.\n Press any key and enter to exit.")
