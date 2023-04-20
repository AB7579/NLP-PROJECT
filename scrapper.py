import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape the data from
url = "https://kiswahili.tuko.co.ke/tags/habari-za-tanzania/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the text and labels from the HTML content
documents = []
labels = []
for paragraph in soup.find_all('p'):
    text = paragraph.text
    label = paragraph.get('class')[0]
    documents.append(text)
    labels.append(label)

# Create a pandas DataFrame to store the data
data = pd.DataFrame({'text': documents, 'label': labels})

# Save the data to a CSV file
data.to_csv('/workspaces/codespaces-jupyter/data/sentiment-data.csv', index=False)
