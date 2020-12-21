from bilibili_api import user
import os
import requests

try:
    os.mkdirs('profile_pics')
except:
    pass
uid_file = open('UID.txt', 'r')
while True:
    uid = uid_file.readline().rstrip()
    if not uid:
        break
    url = user.get_user_info(uid)['face']
    pic = requests.get(url)
    filename = f"{uid}.jpg"
    pic_file = open(f'profile_pics/{filename}', 'wb')
    pic_file.write(pic.content)
    pic_file.close()
    print(f'Downloaded {filename}')
print('All done :D')
