import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "22349465")) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "3732e079c4125690226d8e7b4e028ca4") #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7672442204:AAGYNqb1G_sszCLgHNdId5idnYP_NmG7nRI") # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("ADMINS") else [] #Keep thia empty otherwise bot will not work for owner.
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "tjbot")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://teekam9079:teekam@teekam.cludf.mongodb.net/?retryWrites=true&w=majority&appName=Teekam") # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", "5469498838")) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6390495622)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001786924542")) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "IndiaEarnX") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "False") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://envs.sh/H5.jpg') # image when someone hit /start
LINK_BYPASS = "True" 
"""
   _____                    __  __         _    _              _       _______           _     
  / ____|                  |  \/  |       | |  | |            ( )     |__   __|         | |    
 | |  __  _ __  ___  _   _ | \  / |  __ _ | |_ | |_  ___  _ __|/ ___     | |  ___   ___ | |__  
 | | |_ || '__|/ _ \| | | || |\/| | / _` || __|| __|/ _ \| '__| / __|    | | / _ \ / __|| '_ \ 
 | |__| || |  |  __/| |_| || |  | || (_| || |_ | |_|  __/| |    \__ \    | ||  __/| (__ | | | |
  \_____||_|   \___| \__, ||_|  |_| \__,_| \__| \__|\___||_|    |___/    |_| \___| \___||_| |_|
                      __/ |                                                                    
                     |___/                                                                     
Author: GreyMatter's Tech
GitHub: https://GreyMattersTech.com/GitHub
Website: https://GreyMattersTech.com
"""
