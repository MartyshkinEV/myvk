def market_add(owner_id,params):

    import requests
    from config import token, urlVk

    url=f'{urlVk}market.add?owner_id={owner_id}'
    resp=requests.get(url,params)
    return resp.json()


params={'name':'name', 'description':'description','price':123,'category_id':'Аксессуары'}

