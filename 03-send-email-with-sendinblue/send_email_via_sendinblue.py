from Email import Email
from SendInBlue import SendInBlue


def send_email_via_sendinblue( subject, sender, recipient, reply_to):
    email = Email()
    sendInBlue = SendInBlue()
    email.send_email_via_sendinblue(subject, sender, recipient, reply_to, sendInBlue)


contact_details = {"name": "Stella Stoyneva" , "email": "stella.stoyneva@gmail.com"}
send_email_via_sendinblue("Subject", contact_details, contact_details, contact_details)
