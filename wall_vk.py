def wall_post(group_id, params):
    # параметры указываются такие как мессадже и атачментс Скрипт размещает информацию на стене
    import requests
    from config import token






    wall_post = f'https://api.vk.com/method/wall.post?owner_id=-{group_id}&access_token={token}&v=5.131'

    reg = requests.get(wall_post,params)
    jrep = reg.json()
    print(jrep)
    print(f'https://vk.com/public{group_id}')




def wall_get(owner_id,count=100):
    'Возвращает список записей со стены пользователя или сообщества.'
    from config import token
    import requests
    import time
    import datetime

    wall_get = f'https://api.vk.com/method/wall.get?owner_id=-{owner_id}&count={count}&offset=0&filter=others&access_token={token}&v=5.131'
    resp=requests.get(wall_get)
    print(resp.json())

    items = (resp.json()['response']['items'])
    n = 0
    item = []
    for x in (items):
        n += 1

        sec = (x['date'])
        a = time.ctime(sec)
        d = datetime.datetime.fromtimestamp(sec)

        x['date'] = (d.strftime('%d-%m-%Y'))
        item.append(x)





    return item





# wall_get(130126122)
def groups_getMembers(owner_id):
    from config import token
    import requests
    url= f'https://api.vk.com/method/groups.getMembers?group_id={owner_id}&access_token={token}&v=5.131'
    resp=requests.get(url)
    print(resp.json())

# groups_getMembers('poputnyi_gruz_chelyabinsk')
def wall_seach(owner_id,query,count=10):
    from config import token
    import requests
    url = f'https://api.vk.com/method/wall.search?owner_id=-{owner_id}&access_token={token}&v=5.131'
    params={'query':query,
            'count':count}
    res=requests.get(url,params)
    return (res.json()['response'])

def wall_createComment(owner_id,post_id,message,from_group=0):
    from config import token
    import requests
    url = f'https://api.vk.com/method/wall.createComment?owner_id={owner_id}&access_token={token}&v=5.131'
    params={'post_id':post_id,
            'message':message,
            'from_group':from_group}
    res=requests.get(url,params)
    print(f'https://vk.com/club{str(owner_id)[1:]}?w=wall{owner_id}_{post_id}')
    try:
        capch=res.json()['error']['error_msg']
    except:
        capch=0
    if capch == 'Captcha needed':
        print('Введите капчу')
        captcha_sid = res.json()['error']['captcha_sid']
        captcha_img=res.json()['error']['captcha_img']
        print(captcha_img)
        captcha_key=input()
        params['captcha_sid']=captcha_sid
        params['captcha_key']=captcha_key
        pis=requests.get(url,params)
        print(pis.json())

    print(res.json())