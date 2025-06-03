"""
Unique request number for the each request <CODE><YYYYMMDD><nnnnnnn> 
• MEMBERCODE : Member code (Length : 5) 
• YYYYMMDD : Date format 
• nnnnnnn : Sequence no. starting from one i.e. For first request of the day, it should be (0000001). 
"""
import os
from dotenv import load_dotenv
from datetime import datetime

# Load variables from .env file
load_dotenv()

# Global variable to store sequence number
initial_request_number = 1

# Member Code from the .env file
member_code = str(os.getenv('DEV_MEMBER_CODE'))

# Function to generate the unique request number
def generate_request_number():
    global initial_request_number  # Access the global variable

    # Get the current date
    now = datetime.now()

    # Format the date to YYYYMMDD
    formatted_date = now.strftime("%Y%m%d")

    # Create a 7-digit sequence number (pad with leading zeros)
    sequence_number = f"{initial_request_number:07d}"

    # Construct the unique request number
    msgid = f"{member_code}{formatted_date}{sequence_number}"

    # Increment the sequence number for the next call
    initial_request_number += 1

    return msgid

