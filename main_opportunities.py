
import csv
import requests
from dotenv import load_dotenv
import os

# Load the env file
load_dotenv()
# Replace with your Zoho CRM access token and the CSV file path
access_token = os.environ.get("access_token")
csv_file_path = os.environ.get("csv_file_path")

# Read the CSV file
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Create a new record in the Leads module
        url = 'https://www.zohoapis.com/crm/v2/Deals'
        headers = {
            'Authorization': f'Zoho-oauthtoken {access_token}',
            'Content-Type': 'application/json'
        }

        # Convert the row data to JSON
        data = {
            "data": [dict(row)]
        }

        # Make the API request
        response = requests.post(url, headers=headers, json=data)

        # Print the status code and response JSON
        print(response.status_code, response.json())