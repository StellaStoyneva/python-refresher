from SendInBlue import SendInBlue
from HTMLMixIn import HTMLMixIn
from constants import HTML_PATH, TXT_PATH, SENDINBLUE_API_KEY
class Email(HTMLMixIn):
    def __init__(self):
        self.__html_content = None
        self.__plain_text_content = None
    
    def get_content(self):
        return self._content
      
    def set_html_content(self, content):
        self._content = content

    def set_plain_text_content(self, content):
        self.__plain_text_content = content

    def validate_content_type(self, content_type):
        if(content_type not in ['html', 'text']):
            raise Exception("Invalid type content. Content can only be 'html' or 'text'" )

    def get_content_source_code(self, content_type):
        path = HTML_PATH if content_type =='html' else TXT_PATH
        file = open(path, 'r', encoding='utf-8')
        source_code = file.read()

        return source_code

    def set_email_content(self, content_type):
        self.validate_content_type(content_type)
        source_code = self.get_content_source_code(content_type)
        if content_type =='html': 
            HTMLMixIn.validate_html_content(source_code) 
            self.set_html_content(source_code)
            return
        self.set_plain_text_content(source_code)

    def send_email(self, content_type, sendInBlue):
        self.set_email_content(content_type)
        sendInBlue.configure(SENDINBLUE_API_KEY)
        sendInBlue.send_email_via_sendinblue(self.__html_content, self.__plain_text_content)


email = Email()
sendInBlue = SendInBlue()

email.send_email('text', sendInBlue)