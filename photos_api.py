def create_album(group_id,title):
    import requests
    from config import token
    resp = requests.get(f'https://api.vk.com/method/photos.createAlbum?title={title}&group_id={group_id}&access_token={token}&v=5.131')
    return (resp.json())

def photos_getAlbums(group_id):
    import requests
    from config import token

    res = f'https://api.vk.com/method/photos.getAlbums?owner_id=-{group_id}&access_token={token}&v=5.131'
    respos = requests.get(res)
    return (respos.json())

# photos_getAlbums(214298287)
def photos_get(group_id,album_id):
    from  config import token
    import requests
    resk = f'https://api.vk.com/method/photos.get?owner_id=-{group_id}&album_id={album_id}&access_token={token}&v=5.131'
    x_yi = requests.get(resk)
    return x_yi.json()

def photos_uploadServer(group_id,album_id):
    from config import token
    import requests
    getser = f'https://api.vk.com/method/photos.getUploadServer?group_id={group_id}&album_id={album_id}&access_token={token}&v=5.131'
    rest = requests.get(getser)
    return rest.json()


def save_photo_vk(lotID, groupID, albumID):
    import os
    import requests
    from config import token
    print('photos_uploadServer',photos_uploadServer(groupID, albumID))
    upload_url = (photos_uploadServer(groupID, albumID))['response']['upload_url']
    print(upload_url)
    direc = os.listdir(f'new/{lotID}/')
    print(direc)
    for pict in direc:
        file = {'file1': open(f'new/{lotID}/{pict}', 'rb')}
        ur = requests.post(upload_url, files=file).json()
        result = requests.get(f'https://api.vk.com/method/photos.save', params={'access_token': token,
                                                                                'album_id': ur['aid'],
                                                                                'group_id': ur['gid'],
                                                                                'server': ur['server'],
                                                                                'photos_list': ur[
                                                                                    'photos_list'],
                                                                                'hash': ur['hash'],
                                                                                'caption': pict,
                                                                                'v': '5.131'}).json()
        print(result)