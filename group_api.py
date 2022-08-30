def search_group(zapros, count_f,offset=0):
    from config import token
    import requests
    from myvk.wall_vk import wall_get
    from myvk.mongo_class import apend_list



    url = f'https://api.vk.com/method/groups.search?q={zapros}&count={count_f}&offset={offset}&country_id=1&access_token={token}&v=5.131'

    respo = requests.get(url)
    print(respo.json())

    wool=respo.json()['response']['items']





    return wool
def search_group_city(zapros,count_f,city_id,country_id):
    from config import token
    import requests




    url = f'https://api.vk.com/method/groups.search?&access_token={token}&v=5.131'
    params={'q':zapros,'count':count_f,
            'city_id':city_id,'country_id':country_id}

    respo = requests.get(url,params)
    wool=respo.json()['response']['items']
    return wool



class GetAlbums():
    response=''
    count=''
    items=''
    comments_disabled = []
    thumb_is_last = []
    thumb_id = []
    size = []
    can_delete = []
    created = []
    upload_by_admins_only = []
    description = []
    id_group = []
    updated = []
    can_upload = []
    owner_id = []
    title = []







    def __init__(self, group_id):
        from config import token
        import requests
        url = f'https://api.vk.com/method/photos.getAlbums?owner_id=-{group_id}&access_token={token}&v=5.131'
        resp = requests.get(url)

        jresp= resp.json()
        self.response = jresp['response']
        self.count=self.response['count']
        self.items=self.response['items']
        list_key=[]
        for x in self.items:
            try:
                self.thumb_is_last.append(x["thumb_is_last"])
            except:
                self.thumb_is_last.append("None")
            try:
                self.can_delete.append(x["can_delete"])
            except:
                self.can_delete.append("None")
            try:
                self.can_upload.append(x["can_upload"])
            except:
                self.can_upload.append("None")
            try:
                self.size.append(x["size"])
            except:
                self.size.append("None")
            try:
                self.comments_disabled.append(x["comments_disabled"])
            except:
                self.comments_disabled.append("None")
            try:
                self.description.append(x["description"])
            except:
                self.description.append("None")
            try:
                self.upload_by_admins_only.append(x["upload_by_admins_only"])
            except:
                self.upload_by_admins_only.append("None")
            try:
                self.thumb_id.append(x["thumb_id"])
            except:
                self.thumb_id.append("None")
            try:
                self.created.append(x["created"])
            except:
                self.created.append("None")
            try:
                self.id_group.append(x["id"])
            except:
                self.id_group.append("None")
            try:
                self.owner_id.append(x["owner_id"])
            except:
                self.owner_id.append("None")
            try:
                self.title.append(x["title"])
            except:
                self.title.append("None")
            try:
                self.updated.append(x["updated"])
            except:
                self.updated.append("None")

def groups_join(group_id):
    from config import token
    import requests

    url = f'https://api.vk.com/method/groups.join?&access_token={token}&v=5.131'
    params={'group_id':group_id}
    resp=requests.get(url,params)
    print(resp.json())
    return (resp.json())

def groups_get(owner_id,extended=1,fields='city',offset=0):
    'Возвращает список сообществ указанного пользователя'
    import requests
    from config import token
    url = f'https://api.vk.com/method/groups.get?&access_token={token}&v=5.131'
    params = {'owner_id': owner_id,'extended':extended, 'fields':fields,'offset':offset}
    respo = requests.get(url, params)
    return (respo.json()['response']['items'])


