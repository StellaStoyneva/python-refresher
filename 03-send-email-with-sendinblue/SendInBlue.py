from __future__ import print_function
from copy import Error
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

class SendInBlue:
    def __init__(self):
        self.__configuration = None
    
    def __set_configuration(self):
        self.__configuration = sib_api_v3_sdk.Configuration()

    def configure(self, api_key):
        self.__set_configuration()
        self.__configuration.api_key['api-key'] = api_key

    def send_email_via_sendinblue(self, subject, html_content, plain_text_content, sender_email, recipient_email, reply_to):
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(self.__configuration))
        headers = {"Some-Custom-Name":"unique-id-1234"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(text_content=plain_text_content, to=[recipient_email],  reply_to=reply_to, headers=headers, html_content=html_content, sender=sender_email, subject=subject)

        try:
            api_instance.send_transac_email(send_smtp_email)
            print('Email successfully sent')
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)