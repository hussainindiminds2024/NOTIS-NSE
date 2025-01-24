
def data_parser(response):
    
    trades_inquiry_data = response['data']['tradesInquiry']

    # Split the string into parts
    parts = trades_inquiry_data.split("^")

    # The first part is the data tag
    data_tag = parts[0]

    # The remaining parts are the data lines
    data_lines = parts[1:]

    # Combine the data tag and cleaned data lines
    output = [data_tag] + data_lines

    # Join the lines with newlines
    result = "\n".join(output)

    # Print the reformatted output
    print(type(result))

    return result
