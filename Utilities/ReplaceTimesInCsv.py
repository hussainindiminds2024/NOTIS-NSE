from Utilities import JiffyToDateTime 
from Utilities import MillisecondsToDateTime 

def replace_times_in_csv_string(parsed_response: str) -> str:
    updated_lines = []

    for line in parsed_response.strip().splitlines():
        if not line.strip():
            continue
        parts = line.split(',')

        try:
            # Convert 4th and 18th fields if they exist and are integers
            if len(parts) > 3 and parts[3].isdigit():
                parts[3] = JiffyToDateTime.jiffy_to_datetime(int(parts[3]))
            if len(parts) > 17 and parts[17].isdigit():
                parts[17] = MillisecondsToDateTime.convert_from_1980_seconds(int(parts[17]))

        except Exception as e:
            print(f"Skipping line due to error: {e}")

        updated_lines.append(",".join(parts))

    return "\n".join(updated_lines)