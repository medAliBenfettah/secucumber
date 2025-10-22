import os
import dotenv

dotenv.load_dotenv()

class Config:
    
    #ENVIRONMENT VARIABLES
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
    BROWSER = os.getenv("BROWSER", 'chrome').lower()
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    
    #TIMEOUTS
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 10))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", 10))
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", 30))
    
    #USER CREDENTIALS
    USERNAME = os.getenv("USERNAME","Admin")
    PASSWORD = os.getenv("PASSWORD","admin123")
    
