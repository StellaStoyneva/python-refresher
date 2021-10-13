import os
from dotenv import load_dotenv

load_dotenv()

HTML_PATH = os.path.abspath("python-refresher/03-send-email-with-sendinblue/document.html")
TXT_PATH = os.path.abspath("python-refresher/03-send-email-with-sendinblue/text.txt")

SENDINBLUE_API_KEY=os.getenv('SENDINBLUE_API_KEY')

