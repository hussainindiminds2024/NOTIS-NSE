# Function to create date-based subfolders
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

# Get today's date in the format YYYY-MM-DD
today_date = datetime.now().strftime('%Y-%m-%d')

def create_date_based_folders():
    base_folders = [
        os.getenv('CM_TRADE_INQUIRY_FILE_ALL'),
        os.getenv('CM_TRADE_INQUIRY_FILE_TM'),
        os.getenv('FO_TRADE_INQUIRY_FILE_ALL'),
        os.getenv('FO_TRADE_INQUIRY_FILE_TM')
    ]
    
    # Create the date-based folders if they don't exist
    new_paths = []
    for folder in base_folders:
        folder_path = os.path.join(folder, today_date)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        new_paths.append(folder_path)
    
    return new_paths
