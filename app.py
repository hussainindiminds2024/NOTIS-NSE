from UserDefinedService.CM.CMTradeInquiryResonseService import get_cm_trade_inquiry_response
from UserDefinedService.FO.FOTradeInquiryResponseService import get_fo_trade_inquiry_response

from UserDefinedService import AccessToken

from Utilities import NonceGenerator
from Utilities import MessageIDGenerator
from Utilities import FileWriter
from Utilities import FolderPathUtility

import time
import asyncio

access_token = AccessToken.get_access_token()

# File paths for CM and FO with today's date
cm_all_trade_inquiry_path, cm_tm_trade_inquiry_path, fo_all_trade_inquiry_path, fo_tm_trade_inquiry_path = FolderPathUtility.create_date_based_folders()


async def main():
    extension = ".txt"

    while True:
        try:
            msgid = MessageIDGenerator.generate_request_number()
            nonce = NonceGenerator.get_N_Once()

            # CM Trade Inquiries
            cm_all_trade_inquiry_response = await get_cm_trade_inquiry_response(access_token, "ALL", nonce, msgid)
            await FileWriter.write_content(cm_all_trade_inquiry_response, cm_all_trade_inquiry_path, f"CM_ALL_TRADES{extension}")

            cm_tm_trade_inquiry_response = await get_cm_trade_inquiry_response(access_token, "TMTRADES", nonce, msgid)
            await FileWriter.write_content(cm_tm_trade_inquiry_response, cm_tm_trade_inquiry_path, f"CM_TM_TRADES{extension}")

            # FO Trade Inquiries
            fo_all_trade_inquiry_response = await get_fo_trade_inquiry_response(access_token, "ALL", nonce, msgid)
            await FileWriter.write_content(fo_all_trade_inquiry_response, fo_all_trade_inquiry_path, f"FO_ALL_TRADES{extension}")

            fo_tm_trade_inquiry_response = await get_fo_trade_inquiry_response(access_token, "TMTRADES", nonce, msgid)
            await FileWriter.write_content(fo_tm_trade_inquiry_response, fo_tm_trade_inquiry_path, f"FO_TM_TRADES{extension}")

            # Wait for 5 seconds before the next iteration
            await asyncio.sleep(5)

        except Exception as e:
            print(f"Unexpected error in main loop: {e}")
            await asyncio.sleep(10)  # Wait before retrying on error

# Entry point for the asyncio program
if __name__ == "__main__":
    asyncio.run(main())