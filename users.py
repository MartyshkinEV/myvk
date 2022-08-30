import time
import random
from config import token
import requests
from friends import friends_add
url=f'https://api.vk.com/method/users.search?&access_token={token}&v=5.131'
prompt='объявления'
params={'q':prompt,'offset':random.randint(3, 1000)}
req=requests.get(url,params)

for x in (req.json()['response']['items']):
    time.sleep(random.randint(3, 11))
    friends_add(x['id'])