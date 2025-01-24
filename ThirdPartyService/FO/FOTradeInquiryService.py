import sys
import os
import asyncio
import aiohttp
from dotenv import load_dotenv

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Load environment variables
load_dotenv()

async def fo_trade_inquiry(access_token, fileparameter, nonce, msgid):
    # Set up the endpoint
    base_url = os.getenv('DEV_API_BASE_URL')
    entrypoint = "/inquiry-fo/trades-inquiry"
    endpoint = f"{base_url}{entrypoint}"
    print(endpoint)

    # Headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "nonce": nonce,
        "Content-Type": "application/json"  # Explicitly set Content-Type to JSON
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

    # Send POST request with JSON payload using aiohttp
    async with aiohttp.ClientSession() as session:
        async with session.post(endpoint, json=payload, headers=headers) as response:
            if response.status == 200:
                response_data = await response.json()  # Await the JSON response
                return response_data  # Assuming the response is in JSON format
            else:
                print(f"Status Code: {response.status}, Error: {await response.text()}")
                return "Failed to retrieve Data"
