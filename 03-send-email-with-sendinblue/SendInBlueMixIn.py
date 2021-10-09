from __future__ import print_function
from copy import Error
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

class SendInBlueMixIn:
    def send_email_via_sendinblue(html_content, plain_text_content, sender_email, api_key):
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = api_key
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        subject = "My Subject"
        sender = {"name":"John Doe","email":sender_email}
        to = [{"email":sender_email,"name":"Jane Doe"}]
        reply_to = {"email":sender_email,"name":"John Doe"}
        headers = {"Some-Custom-Name":"unique-id-1234"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(text_content=plain_text_content, to=to,  reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

        try:
            api_instance.send_transac_email(send_smtp_email)
            print('Email successfully sent')
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)