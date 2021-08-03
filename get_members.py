from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

from telethon.errors import SessionPasswordNeededError
import csv

from constant import API_HASH, APP_ID, PASSWORD, PHONE_NO

api_id = APP_ID
api_hash = API_HASH
phone = PHONE_NO
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=PASSWORD)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(
    GetDialogsRequest(offset_date=last_date,
                      offset_id=0,
                      offset_peer=InputPeerEmpty(),
                      limit=chunk_size,
                      hash=0))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
        if chat.broadcast == True:
            groups.append(chat)
    except:
        continue

print('Choose a group to scrape members from:')
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Enter a Number: ")
target_group = groups[int(g_index)]

print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In file...')
with open("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow([
        'username', 'user_id', 'access_hash', 'name', 'group', 'group_id',
        'phone_number'
    ])
    for user in all_participants:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([
            username, user.id, user.access_hash, name, target_group.title,
            target_group.id, user.phone
        ])
print('Members scraped successfully.')
