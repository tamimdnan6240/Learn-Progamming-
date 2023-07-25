import requests
from zipfile import ZipFile
import pandas as pd

# Step 1: Install necessary libraries (only required if not already installed)
!pip install requests
!pip install pandas

# Step 2: Download and unzip the dataset
url = "https://files.ontario.ca/opendata/tts_dataset.zip"
response = requests.get(url)

# Save the downloaded zip file
with open('tts_dataset.zip', 'wb') as f:
    f.write(response.content)

# Unzip the downloaded file
with ZipFile('tts_dataset.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Step 3: Load the data using pandas - repeat for all data 
# use pd.csv("/path/")
# data = pd.csd("/path") 
# print (data)
