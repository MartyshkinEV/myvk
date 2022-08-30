def db_city(country_id,q):
    from config import token
    import requests
    url = f'https://api.vk.com/method/database.getCities?&access_token={token}&v=5.131'
    params={'country_id':country_id,'q':q}

    respo=requests.get(url,params)
    print(respo.json())



def db_getRegion(country_id,q):
    from config import token
    import requests
    url = f'https://api.vk.com/method/database.getRegions?&access_token={token}&v=5.131'
    params={'country_id':country_id,'q':q}

    respo=requests.get(url,params)
    print(respo.json())

