import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from ThirdPartyService.CM.CMActionInquiryService import cm_action_inquiry

async def get_cm_action_inquiry_response(access_token, fileparameter, nonce, msgid):
    response = cm_action_inquiry(access_token, fileparameter, nonce, msgid)
    return response

