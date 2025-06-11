from UserDefinedService.CM.CMTradeInquiryResonseService import get_cm_trade_inquiry_response
from UserDefinedService.FO.FOTradeInquiryResponseService import get_fo_trade_inquiry_response

from UserDefinedService import AccessToken

from Utilities import NonceGenerator
from Utilities import MessageIDGenerator
from Utilities import FileWriter
from Utilities import FolderPathUtility
from Utilities import DataParser

import time
from datetime import datetime, timedelta
import asyncio

# File paths for CM and FO with today's date
cm_all_trade_inquiry_path, cm_tm_trade_inquiry_path, fo_all_trade_inquiry_path, fo_tm_trade_inquiry_path = FolderPathUtility.create_date_based_folders()


async def main():
    extension = ".csv"
    log_extension = ".txt"
    access_token = AccessToken.get_access_token()
    last_token_refresh_time = datetime.now()

    initial_ALL_CM_tradeSeq = 0
    initial_TM_CM_tradeSeq = 0
    initial_ALL_FO_tradeSeq = 0
    initial_TM_FO_tradeSeq = 0

    while True:
        try:
            now = datetime.now()

            # Refresh token every 30 minutes
            if now - last_token_refresh_time >= timedelta(minutes=30):
                print("Refreshing access token...")
                access_token = AccessToken.get_access_token()
                last_token_refresh_time = now

            msgid = MessageIDGenerator.generate_request_number()
            print(f"\n========== New Iteration ==========")
            print(f"Executing with message ID: {msgid}")
            nonce = NonceGenerator.get_N_Once()

            # === CM ALL ===
            print(f"\n--- CM ALL ---")
            print(f"Initial ALL_CM_TradeSeq used for API: {initial_ALL_CM_tradeSeq}")

            cm_all_trade_inquiry_response = await get_cm_trade_inquiry_response(
                access_token, "ALL", nonce, msgid, int(initial_ALL_CM_tradeSeq)
            )

            max_trade_seq_all_cm, _ = DataParser.data_parser(cm_all_trade_inquiry_response)

            print(f"MaxTradeSeq returned from CM ALL DataParser: {max_trade_seq_all_cm}")

            initial_ALL_CM_tradeSeq = max_trade_seq_all_cm
            print(f"Updated initial_ALL_CM_tradeSeq: {initial_ALL_CM_tradeSeq}")

            # Optional: Save to file for audit or debugging
            await FileWriter.write_content(cm_all_trade_inquiry_response, cm_all_trade_inquiry_path, f"CM_ALL_TRADES{extension}")
            
            print("✅ CM ALL trades written to file")

            await FileWriter.append_content(cm_all_trade_inquiry_response, cm_all_trade_inquiry_path, f"CM_ALL_TRADES_LOG{log_extension}")

            print("✅ CM ALL trades written to log file")
            # === CM TM ===
            # print(f"\n--- CM TM ---")
            # print(f"Initial TM_CM_TradeSeq used for API: {initial_TM_CM_tradeSeq}")

            # cm_tm_trade_inquiry_response = await get_cm_trade_inquiry_response(
            #     access_token, "TMTRADES", nonce, msgid, int(initial_TM_CM_tradeSeq)
            # )

            # max_trade_seq_tm_cm, _ = DataParser.data_parser(cm_tm_trade_inquiry_response)

            # print(f"MaxTradeSeq returned from CM TM DataParser: {max_trade_seq_tm_cm}")

            # initial_TM_CM_tradeSeq = max_trade_seq_tm_cm
            # print(f"Updated initial_TM_CM_tradeSeq: {initial_TM_CM_tradeSeq}")

            # # Optional: Save to file for audit or debugging
            # await FileWriter.write_content(cm_tm_trade_inquiry_response, cm_tm_trade_inquiry_path, f"CM_TM_TRADES{extension}")
            # print("✅ CM TM trades written to file")

            # === FO ALL ===
            print(f"\n--- FO ALL ---")
            print(f"Initial ALL_FO_TradeSeq used for API: {initial_ALL_FO_tradeSeq}")

            fo_all_trade_inquiry_response = await get_fo_trade_inquiry_response(
                access_token, "ALL", nonce, msgid, int(initial_ALL_FO_tradeSeq)
            )

            max_trade_seq_all_fo, _ = DataParser.data_parser(fo_all_trade_inquiry_response)

            print(f"MaxTradeSeq returned from FO ALL DataParser: {max_trade_seq_all_fo}")

            initial_ALL_FO_tradeSeq = max_trade_seq_all_fo
            print(f"Updated initial_ALL_FO_tradeSeq: {initial_ALL_FO_tradeSeq}")

            # Optional: Save to file for audit or debugging
            await FileWriter.write_content(fo_all_trade_inquiry_response, fo_all_trade_inquiry_path, f"FO_ALL_TRADES{extension}")
            print("✅ FO ALL trades written to file")

            await FileWriter.append_content(fo_all_trade_inquiry_response, fo_all_trade_inquiry_path, f"FO_ALL_TRADES_LOG{log_extension}")

            print("✅ FO ALL trades written to log file")

            # === FO TM ===
            # print(f"\n--- FO TM ---")
            # print(f"Initial TM_FO_TradeSeq used for API: {initial_TM_FO_tradeSeq}")

            # fo_tm_trade_inquiry_response = await get_fo_trade_inquiry_response(
            #     access_token, "TMTRADES", nonce, msgid, int(initial_TM_FO_tradeSeq)
            # )

            # max_trade_seq_tm_fo, _ = DataParser.data_parser(fo_tm_trade_inquiry_response)

            # print(f"MaxTradeSeq returned from FO TM DataParser: {max_trade_seq_tm_fo}")

            # initial_TM_FO_tradeSeq = max_trade_seq_tm_fo
            # print(f"Updated initial_TM_FO_tradeSeq: {initial_TM_FO_tradeSeq}")

            # # Optional: Save to file for audit or debugging
            # await FileWriter.write_content(fo_tm_trade_inquiry_response, fo_tm_trade_inquiry_path, f"FO_TM_TRADES{extension}")
            # print("✅ FO TM trades written to file")

            # Wait for 30 seconds before next iteration
            print("\n✅ Sleeping for 5 seconds...\n")
            await asyncio.sleep(5)

        except Exception as e:
            print(f"\n⚠️  Unexpected error in main loop: {e}")
            print("Sleeping for 10 seconds before retry...\n")
            await asyncio.sleep(10)  # Wait before retrying on error


# Entry point for the asyncio program
if __name__ == "__main__":
    asyncio.run(main())
