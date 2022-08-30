def friends_add(user_id):
    from config import token
    import requests
    url = f'https://api.vk.com/method/friends.add?&access_token={token}&v=5.131'
    params={'user_id':user_id}
    req=requests.get(url,params)
    print(req.json())
    return req.json()

