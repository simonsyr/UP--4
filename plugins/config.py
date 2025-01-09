import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    API_ID = int(os.environ.get("API_ID", "19441363"))
    
    API_HASH = os.environ.get("API_HASH", "a23b4f5397930e1fd722e764ba644f37")
    
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1002003641610")
    
    MAX_FILE_SIZE = 50000000
    
    TG_MAX_FILE_SIZE = 4717156800
    
    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "URL_UPLOAD_TG_BOT"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "URL_UPLOAD_TG_BOT")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002003641610")
    
    AUTH_USERS = int(os.environ.get("AUTH_USERS", "6470677872"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "URL_UPLOAD_TG_BOT")
                                  
