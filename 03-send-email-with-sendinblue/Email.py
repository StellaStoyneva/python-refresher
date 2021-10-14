# pylint: disable=wildcard-import
from HTMLMixIn import HTMLMixIn
from constants import TXT_PATH, HTML_PATH, SENDINBLUE_API_KEY


class Email(HTMLMixIn):
    def __init__(self):
        self.__html_content = None
        self.__plain_text_content = None
    
    def get_html_content(self):
        return self.__html_content

    def set_html_content(self, content):
        self.__html_content = content

    def get_text_content(self):
        return self.__plain_text_content

    def set_plain_text_content(self, content):
        self.__plain_text_content = content

    def set_email_contents(self):
        text_file = open(TXT_PATH, 'r', encoding='utf-8')
        text_source_code = text_file.read()
        self.set_plain_text_content(text_source_code)

        html_file = open(HTML_PATH, 'r', encoding='utf-8')
        html_source_code = html_file.read()
        HTMLMixIn.validate_html_content(html_source_code)
        self.set_html_content(html_source_code)

    def send_email_via_sendinblue(self, subject, sender, recipient, reply_to, sendInBlue):
        self.set_email_contents()
        sendInBlue.configure(SENDINBLUE_API_KEY)
        sendInBlue.send_email(subject, self.__html_content, self.get_text_content(), sender, recipient, reply_to)
