from dotenv import load_dotenv
#Loading the enviorment file
load_dotenv()
import os
import pyodbc

server = os.getenv('SERVER') 
database = os.getenv('DATABASE') 
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD') 
driver = os.getenv('DRIVER') 

def get_connection():
    # Establish connection
    connection = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;')
    print('Connection Succesful!')
    return connection

