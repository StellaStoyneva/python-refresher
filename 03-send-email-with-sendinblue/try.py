from dotenv import load_dotenv
import os

load_dotenv()

SENDINBLUE_API_KEY=os.getenv('SENDINBLUE_API_KEY')
print (SENDINBLUE_API_KEY)