import sys
import os

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

import requests
from dotenv import load_dotenv
# Load environment variables
load_dotenv()


def cm_action_inquiry(access_token,fileparameter,nonce,msgid):
    # Set up the endpoint
    base_url = os.getenv('DEV_API_BASE_URL')
    entrypoint = "/notis-cm/actions-inquiry"
    endpoint = f"{base_url}{entrypoint}"
    print(endpoint)
    nonce = nonce
    # Headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "nonce": nonce,
        "Content-Type": "application/json"  # Explicitly set Content-Type to JSON
    }
    # Parameters
    params = {
        "grant_type": "client_credentials"
    }
    # Request Payload (ensure proper structure)
    payload = {
        "version": "2.1",
        "data": {
            "msgId": f"{msgid}",
            "dataFormat": "CSV:CSV",
            "tradesInquiry": f"0,{fileparameter},,"
        }
    }
    # Send POST request with JSON payload
    response = requests.post(endpoint, params=params, json=payload, headers=headers)
    # Check the response
    if response.status_code == 200:
        return response.json()  # Assuming the response is in JSON format
    else:
        print(f"Status Code: {response.status_code},Error: {response.text}")
        return "Failed to retreive Data"
    
