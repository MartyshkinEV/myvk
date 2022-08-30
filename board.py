def getTopic(owner_id,order):

    'Возвращает список тем в обсуждениях указанной группы.'
    import requests
    from config import token
     #topic_ids Список идентификаторов тем, которые необходимо получить (не более 100). По умолчанию возвращаются все темы. Если указан данный параметр,
    # игнорируются параметры order, offset  и count (возвращаются все запрошенные темы в указанном порядке).
    url=f'https://api.vk.com/method/board.getTopics?&access_token={token}&v=5.131'
    params={'group_id':owner_id,'order':order}
    respo=requests.get(url,params)

    return respo.json()['response']

def board_getComments(group_id,topic_id,count=100,offset=0):
    from config import token
    import requests
    url = f'https://api.vk.com/method/board.getComments?&access_token={token}&v=5.131'
    params={'group_id':group_id,'topic_id':topic_id,'count':count,'offset':offset}
    respo=requests.get(url,params)
    return  (respo.json())
def board_createComment(group_id,topic_id,message):
    from config import token
    import requests
    url= f'https://api.vk.com/method/board.createComment?&access_token={token}&v=5.131'
    params={'group_id':group_id,
            'topic_id':topic_id,
            'message':message}

    respo=requests.get(url,params)

    return respo.json()




