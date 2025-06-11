from datetime import datetime, timedelta

def convert_from_1980_seconds(seconds_since_1980: int) -> datetime:
    epoch = datetime(1980, 1, 1)
    return str(epoch + timedelta(seconds=seconds_since_1980))

# result = convert_from_1980_seconds(1434013504)
# print(result)
# print(type(result))