class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = ""
    OWNER_ID = "596368682"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Arman_xD"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://evjwrjcdishzwz:6f81aaaf6235bc2a45651e7e5ad955039f372cd9b39ec6042e7c277324dc3ce7@ec2-23-21-156-171.compute-1.amazonaws.com:5432/d6krgja6gi5h24'  # needed for any database modules
    MESSAGE_DUMP = -1001349863386 # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = ANYTHING
    URL = "https://prakasaka.herokuapp.com/"

    # OPTIONAL
    SUDO_USERS = [596368682,759400881,597725966,669056998,387142880,554898593]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADBQADDQADjR\_yKCDDBtuwTt59Ag'  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = '' # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
