import requests
from myvk.wall_vk import wall_post
def polls_getPhotoUploadServer(owner_id):
    import requests
    from config import token
    url = f'https://api.vk.com/method/polls.getPhotoUploadServer?&owner_id={owner_id}&access_token={token}&v=5.131'
    res=requests.get(url)
    print(res.json())
    return res.json()

def polls_savePhoto(photo,hash):
    import requests
    from config import token
    url = f'https://api.vk.com/method/polls.savePhoto?photo={photo}&hash={hash}&access_token={token}&v=5.131'
    res=requests.get(url)
    print(res.json())



def palls_create (question,add_answers):
    from config import token

    'Позволяет создавать опросы, которые впоследствии можно прикреплять к записям на странице пользователя или сообщества'
    url=f'https://api.vk.com/method/polls.create?&owner_id=-215241313&background_id=3&access_token={token}&v=5.131'
    params={'question':question,'add_answers':add_answers}

    respo=requests.get(url, params)
    print(respo.json())
    return respo.json()



'763520752'
