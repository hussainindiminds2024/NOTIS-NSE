import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from ThirdPartyService.FO.FOTradeInquiryService import fo_trade_inquiry

async def get_fo_trade_inquiry_response(access_token, fileparameter, nonce, msgid):
    response = await fo_trade_inquiry(access_token, fileparameter, nonce, msgid)
    return response
