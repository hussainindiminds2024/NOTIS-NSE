import datetime

def jiffy_to_datetime(jiffy: int) -> datetime.datetime:
    # Define the reference date
    reference_date = datetime.datetime(1980, 1, 1, 0, 0, 0)
    
    # Convert jiffy to seconds
    seconds = jiffy / 65536  # This will be a float
    
    # Compute the final datetime by adding the seconds to the reference date
    result_datetime = reference_date + datetime.timedelta(seconds=seconds)
    return str(result_datetime)

# result = jiffy_to_datetime(1434013629)
# print(result)
# print(type(result))