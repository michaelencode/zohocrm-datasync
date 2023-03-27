
import requests
from dotenv import load_dotenv
import os

# Load the env file
load_dotenv()
# Replace with your Zoho CRM access token and the CSV file path
access_token = os.environ.get("access_token")
module_name = "deals"
def get_latest_record_from_module(access_token, module_name):
    base_url = "https://www.zohoapis.com/crm/v2/"
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }

    params = {
        "sort_order": "desc",
        "sort_by": "Created_Time",
        "page": 1,
        "per_page": 1
    }

    url = f"{base_url}{module_name}"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        records = response.json().get("data")
        if records:
            return records[0]
        else:
            print(f"No records found in the {module_name} module.")
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

if __name__ == "__main__":

    latest_record = get_latest_record_from_module(access_token, module_name)
    if latest_record:
        print(f"Latest record in the {module_name} module:")
        print (latest_record)
