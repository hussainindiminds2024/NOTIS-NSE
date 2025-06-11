import os
from Utilities import DataParser
import json
from Utilities import ReplaceTimesInCsv

async def write_content(content, folder_path, file_name):
    # Check if content is a valid JSON
    try:
        # store content as JSON
        response = content
        # If successful, parse the content using your custom parser
        _ , parsed_response = DataParser.data_parser(response)
        #print(parsed_response)
            # Combine folder path and file name to get the full file path
        full_file_path = os.path.join(folder_path, file_name)

        # Ensure the directory exists, if not create it
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

        # Open the file and write the content (parsed or original)
        with open(full_file_path, 'w') as file:
            file.write(parsed_response)
    except json.JSONDecodeError:
        # If JSON decoding fails, treat content as a plain string
        print(content)

async def append_content(content, folder_path, file_name):
    # Check if content is a valid JSON
    try:
        # store content as JSON
        response = content
        print(type(response))
        # If successful, parse the content using your custom parser
        _ , parsed_response = DataParser.data_parser_without_data_tag(response)
        print(type(parsed_response))
        print(parsed_response)
        
        content = ReplaceTimesInCsv.replace_times_in_csv_string(parsed_response)
        # Combine folder path and file name to get the full file path
        full_file_path = os.path.join(folder_path, file_name)

        # Ensure the directory exists, if not create it
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

        # Open the file and write the content (parsed or original)
        with open(full_file_path, 'a') as file:
            file.write(content + '\n')
    except json.JSONDecodeError:
        # If JSON decoding fails, treat content as a plain string
        print(content)