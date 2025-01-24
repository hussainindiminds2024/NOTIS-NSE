Utilities
-------------------------

1. Base64encoder Utility 
--------------------------
It is used to encode the "nonce" generated.

2. N-Once Utility
--------------------------
It is used to generate N-Once(nonce) that will be sent in API requests to NSE Notis.
NOTE:
An N-once value, that uniquely identifies each request sent to server. Has to be a base64 
encoding of the following data: ddMMyyyyHHmmssSSS:<6-digit random number> 

3. Message ID Utility
--------------------------
Used to generate a unique message ID for each request.
NOTE:
Unique request number for the each request <CODE><YYYYMMDD><nnnnnnn> 
• MEMBERCODE : Member code (Length : 5) 
• YYYYMMDD : Date format 
• nnnnnnn : Sequence no. starting from one i.e. For first request of the day, it should be (0000001). 

4. File Write Utility

5. JSON parsing Utility

6. Folder Path Utility

Third party services
------------------------

1. Requesting access token
-----------------------------
Requesting access token using nonce, and Basic Authorization using user_key(Username) and user_secret(Password)



File Nomenclature:
---------------------
CM_ALL_TRADES_{msgid}{extension} -> Response File Nommenclature.


