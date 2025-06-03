
"""
An N-once value, that uniquely identifies each request sent to server. Has to be a base64 
encoding of the following data: ddMMyyyyHHmmssSSS:<6-digit random number> 
"""
import random
from datetime import datetime
from Utilities import Base64encoder

def get_N_Once():
    # Get the current date and time
    now = datetime.now()
    # Format the date and time to ddMMyyyyHHmmssSSS
    formatted_date_time = now.strftime("%d%m%Y%H%M%S") + f"{now.microsecond // 1000:03d}"
    seperator = ":"

    # Generate a 6-digit random number
    random_number = str(random.randint(100000, 999999))

    # Raw N-Once string
    formatted_string = f"{formatted_date_time}{seperator}{random_number}"

    #Encoded N-once string
    encoded_formatted_string = Base64encoder.base64encoder(formatted_string)
    
    return encoded_formatted_string

