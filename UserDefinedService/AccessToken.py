import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from ThirdPartyService import RequestAccessTokenService

def get_access_token():
    response = RequestAccessTokenService.request_access_token()
    # Check if the response is a dictionary indicating an error
    if isinstance(response, dict) and "Error" in response:
        print(f"Failed to retrieve access token. Status Code: {response['Status Code']}, Error: {response['Error']}")
    else:
        # Token was successfully retrieved
        print(f"Access Token retrieved: {response}")
        # Use the token for further processing
        # Example: Pass the token to another API call
        return response
    
    