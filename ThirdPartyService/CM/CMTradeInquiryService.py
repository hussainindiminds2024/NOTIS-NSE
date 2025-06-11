import sys
import os
import asyncio
import aiohttp
from dotenv import load_dotenv

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

# Load environment variables
load_dotenv()

async def cm_trade_inquiry(access_token, fileparameter, nonce, msgid, maxTradeSeq):
    # Set up the endpoint
    base_url = os.getenv('DEV_API_BASE_URL')
    entrypoint = "/notis-cm/trades-inquiry"
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
            "tradesInquiry": f"{maxTradeSeq},{fileparameter},,"
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