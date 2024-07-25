class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5536168611"
    sudo_users = "5536168611", "6765826972"
    GROUP_ID = -1002193507705
    TOKEN = "7204983300:AAGFwLAEIy8_HdVUSKxD4EIdcAR5bVnHwQo"
    mongo_url = "mongodb+srv://Dark123:Dark123@cluster0.jsapbqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "@Shshijdjdbnr_jdj_bot"
    CHARA_CHANNEL_ID = "-1002239117016"
    api_id = 6390608832
    api_hash = "9647ab7fc03a8a93f701a5528b2f206e"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
