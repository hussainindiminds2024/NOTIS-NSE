import sys
import os

# Add the root directory of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from ThirdPartyService.FO.FOActionInquiryService import fo_action_inquiry

def get_fo_action_inquiry_response(access_token, fileparameter, nonce, msgid):
    response = fo_action_inquiry(access_token, fileparameter, nonce, msgid)
    return response