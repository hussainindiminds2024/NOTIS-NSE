import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from Utilities import NonceGenerator

load_dotenv()

def request_access_token():
    # Credentials from the .env file
    Username = os.getenv('DEV_API_KEY')
    Password = os.getenv('DEV_API_SECRET')

    # Base URL from the .env file
    base_url = os.getenv('DEV_API_BASE_URL')

    #URL Endpoint
    token_url = "/token"

    # Full endpoint
    token_endpoint = f"{base_url}{token_url}"

    #Data to be sent in body
    data = {
        "grant_type": "client_credentials"
    }

    # nonce generated using Utility  
    nonce =  NonceGenerator.get_N_Once()

    # Headers 
    headers = {
        "nonce": nonce,
        "Content-Type": "application/x-www-form-urlencoded"  # Specify the content type
    }

    # Send POST request with Basic Auth, data, and headers
    response = requests.post(token_endpoint, data=data, headers=headers, auth=HTTPBasicAuth(Username, Password))

    # Check the response
    if response.status_code == 200:
        print(response.status_code)
        response_data = response.json()
        access_token = response_data['access_token']
        return access_token
    else:
        return {"Status Code": response.status_code , "Error": response.text}
    