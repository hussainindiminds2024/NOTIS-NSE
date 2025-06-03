import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)
from dotenv import load_dotenv
load_dotenv()
from Utilities.Connection import get_connection

class ImportCMTradeResponseRepositoryMethods():
    async def import_all_trades(FilePath):
        conn = get_connection()
        cursor = conn.cursor()
        UserId = os.getenv('USER_ID')
        ExchangeSegment = os.getenv('SEGMENT_ID')
        CompanyId = os.getenv('COMPANY_ID')
        LockTradeDate = os.getenv('LOCK_TRADE_DATE')
        ExpiryDate = os.getenv('EXPIRE_DATE')
        LockMsg = os.getenv('LOCK_MSG')

        query = """
                    EXEC [Import_TradeNSECM_Notis] @ModifyUser = ?, @ExcSegmt = ?, @FilePath = ?, @ExchangeTrades_CompanyID = ?, @LckTradeDate = ?, @ExpireDate = ?, @LockMsg = ? ;
                """
        cursor.execute(query,(UserId ,ExchangeSegment,FilePath,CompanyId,LockTradeDate,ExpiryDate,LockMsg))

        conn.commit()
        print('Import For CM Trade Response in All Segment Successful!')