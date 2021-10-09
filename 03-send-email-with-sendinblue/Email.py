from SendInBlueMixIn import SendInBlueMixIn
from HTMLMixIn import HTMLMixIn
from constants import HTML_PATH, TXT_PATH, SENDINBLUE_API_KEY
class Email(SendInBlueMixIn, HTMLMixIn):
    def __init__(self):
        self.content = ''
    
    def get_content(self):
        return self._content
      
    def set_content(self, x):
        self._content = x

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
        self.set_content(source_code)

    def send_email(self, content_type):
        self.set_email_content(content_type)
        content = self.get_content()
        html_content = content if content_type == 'html' else None
        plain_text_content = None if content_type == 'html' else content
        SendInBlueMixIn.send_email_via_sendinblue(html_content, plain_text_content, "stella.stoyneva@mentormate.com", SENDINBLUE_API_KEY)


email = Email()

email.send_email('text')