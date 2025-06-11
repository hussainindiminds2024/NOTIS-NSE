import json

def data_parser(response):
    
    trades_inquiry_data = response['data']['tradesInquiry']

    # Split the string into parts
    parts = trades_inquiry_data.split("^")

    # The first part is the data tag
    data_tag = str(parts[0])

    split_data_tag_str = data_tag.split(',')

    max_trade_seq = split_data_tag_str[4]

    # The remaining parts are the data lines
    data_lines = parts[1:]

    # Combine the data tag and cleaned data lines
    output = [data_tag] + data_lines

    # Join the lines with newlines
    result = "\n".join(output)

    # Print the reformatted output
    #print(type(result))

    return  max_trade_seq, result

def data_parser_without_data_tag(response):
    
    trades_inquiry_data = response['data']['tradesInquiry']

    # Split the string into parts
    parts = trades_inquiry_data.split("^")

    # The first part is the data tag
    data_tag = str(parts[0])

    split_data_tag_str = data_tag.split(',')

    max_trade_seq = split_data_tag_str[4]

    # The remaining parts are the data lines
    data_lines = parts[1:]

    # Combine the data tag and cleaned data lines
    output = data_lines

    # Join the lines with newlines
    result = "\n".join(output)

    # Print the reformatted output
    #print(type(result))

    return  max_trade_seq, result

# with open("C:/Projects/NOTIS-NSE/SampleResponse/tradeall_response.txt","r") as File:
#     content = File.read()
#     json_content = json.loads(content)

# result = data_parser(json_content)

# with open("C:/Projects/NOTIS-NSE/SampleResponse/parsed_response.txt","w") as File:
#     File.write(result)
