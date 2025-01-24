import base64

def base64encoder(text):
    #Storing it
    string=text
    # Convert the string to bytes and encode it to Base64
    base64_bytes = base64.b64encode(string.encode('utf-8'))
    # Decode the Base64 bytes into a string
    base64_string = base64_bytes.decode('utf-8')
    return base64_string