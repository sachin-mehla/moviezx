import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', 7270745))
API_HASH = environ.get('API_HASH', 'e8d7db1802b0b3839f646a1249e9ef34')
BOT_TOKEN = environ.get('BOT_TOKEN', '5696172983:AAFifkmTHG0GBb8aIM0F4tquQAttyrBw_KY')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://drive.google.com/file/d/1xrO25T-E94LSrxjICDEiXyNnUkwqEl-_/view?usp=drivesdk')).split()

# Admins, Channels & Users
ADMINS = [5698744303]
CHANNELS = [-1001805539468, -1001726863824, -1001726271190]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = -1001805539468
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://rorboy:rorboy@cluster0.2erhwjr.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "rorx")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'hashtag')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001526478235))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '@sachinXmehla')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', 'True')), False)
IMDB = is_enabled((environ.get('IMDB', 'True')), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', 'True')), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '♦️ <em>ꜰɪʟᴇ ɴᴀᴍᴇ</em>: @sachinXmehla | <code>{file_name}</code> \n\n♦️ <em>ꜰɪʟᴇ ꜱɪᴢᴇ : {file_size}</em> \n\n♦️ <em>ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ @moviezXrobot</em>  \n\n♦️ <i>ʀᴇ𝚀ᴜᴇꜱᴛ ᴍᴏᴠɪᴇꜱ @moviesX11_bot</i> \n\n')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '♦️ <em>ꜰɪʟᴇ ɴᴀᴍᴇ</em>: @sachinXmehla | <code>{file_name}</code> \n\n♦️ <em>ꜰɪʟᴇ ꜱɪᴢᴇ : {file_size}</em> \n\n♦️ <em>ᴜᴘʟᴏᴀᴅᴇᴅ ʙʏ @moviezXrobot</em>   \n\n♦️ <i>ʀᴇ𝚀ᴜᴇꜱᴛ ᴍᴏᴠɪᴇꜱ @moviesx11_bot</i> \n\n')
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10  \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [Sachin Mehla](https://t.me/sachinXmehla)")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = int(environ.get('FILE_STORE_CHANNEL', -1001816922327))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
