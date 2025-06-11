import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from ThirdPartyService.CM.CMTradeInquiryService import cm_trade_inquiry

async def get_cm_trade_inquiry_response(access_token, fileparameter, nonce, msgid, maxTradeSeq):
    response = await cm_trade_inquiry(access_token, fileparameter, nonce, msgid, maxTradeSeq)
    return response

