from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22440762"))
    API_HASH = getenv("API_HASH", "f18c585387a50ef82cf4eab05be6dd59")
    BOT_TOKEN = getenv("BOT_TOKEN", "5958352109:AAEW4bqGZaZiIo-IoBpiAWh9rV5iWemjM6U")
    FSUB = getenv("FSUB", "Spyromovies")
    CHID = int(getenv("CHID", "-1001647019088"))
    SUDO = list(map(int, getenv("1361111830").split()))
    MONGO_URI = getenv("MONGO_URI", "d1731c0756deb8ad0651f847d11ab4e7")
    
cfg = Config()
