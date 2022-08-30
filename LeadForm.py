def create_form(group_id):
    from config import token
    import requests
    url = f'https://api.vk.com/method/leadForms.create?&access_token={token}&v=5.131'
    name = "утилита"
    title = 'ого бой и усик'
    description = 'двай запишем это на радио'
    active =1
    policy_link_url='https://ya.ru'
    questions = '[   {      \"type\":\"first_name\"   },   ' \
                '{      \"type\":\"input\",      \"label\":\"откуда\"   },   ' \
                '{      \"type\":\"input\",      \"label\":\"куда\"   },    ' \
                '{      \"type\":\"input\",      \"label\":\"Дата\"   },    ' \
                '{      \"type\":\"input\",      \"label\":\"Время\"   },    ' \
                '{      \"type\":\"input\",      \"label\":\"описание груза\"   }]'

    params = {
        'group_id': group_id,
        'name': 'first',
        'title': 'probnay',
        'description': 'xz chto',  # описание формы
        'questions': questions,
        'policy_link_url':policy_link_url,
        'active':active
        'confirmation':'спасибо ебать ты молодец!'

    }

    response = requests.get(url, params)
    print(response.json())

create_form(215468100)


def leadForms_list(group_id):
    from config import token, group_id
    import requests


    url = f'https://api.vk.com/method/leadForms.list?&group_id={group_id}&access_token={token}&v=5.131'

    respo= requests.get(url)

    print(respo.json())

