import re
from datetime import datetime

async def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

async def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False

async def is_valid_discord(discord):
    pattern = r'^[a-zA-Z0-9._%+-]+#\b\d{4}\b'
    return bool(re.match(pattern, discord))

async def is_steam_link(steam):
    pattern = r'^https?://steamcommunity\.com/(profiles|id)/[a-zA-Z0-9]+/?$'
    return bool(re.match(pattern, steam))

async def is_int_phone(phone):
    if phone[1:].isdigit():
        return True
    else:
        return False
    