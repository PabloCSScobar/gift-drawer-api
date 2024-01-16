from dotenv import load_dotenv
import os
load_dotenv()


EMAIL_API_KEY = os.getenv("EMAIL_API_KEY")
EMAIL_DEBUG_MODE = os.getenv("EMAIL_DEBUG_MODE")
EMAIL_DEBUG_ADDRESS = os.getenv("EMAIL_DEBUG_ADDRESS")
EMAIL_SENDER_ADDRESS = os.getenv("EMAIL_SENDER_ADDRESS")