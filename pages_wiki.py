def wiki_pages():
    from config import token
    import requests
    from myvk.mongo_class import collecsion_conn
    coll = collecsion_conn('vkontacte', 'hard_insert')
    a = ''
    priceMin = ''
    for x in coll.find({'id': '22000125790000000002_1'}):
        a = x['lotDescription']
        priceMin = x['priceMin']

    owner_id =215241313
    print(a)
    url = f'https://api.vk.com/method/pages.save?group_id={owner_id}&text=<sup><b>{a}</b></sup><br/>' \
          f'[[poll-215241313_763520752]][[photo-214298287_457240490|200px;right|www.vk.com]][[photo-214298287_457240489|200px;right|https://www.vk.com]]<br/>{priceMin}<br/>&title="рвая страница"&access_token={token}&v=5.131'

    res = requests.get(url)
    print(res.json())
    print(f'https://vk.com/page-{owner_id}_{res.json()["response"]}')
wiki_pages()

def pages_get():
    from config import token
    import requests
    owner_id=82855000
    url = f'https://api.vk.com/method/pages.get?group_id={owner_id}&page_id=49864254&access_token={token}&v=5.131'
    res=requests.get(url)
    print(res.json())

