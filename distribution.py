from vk_api.bot_longpoll import VkBotLongPoll
import vk_api
import requests

def distribution(message,token_group,id_group,token_app):

    vk_session = vk_api.VkApi(token=token_group)
    session_api = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, id_group)

    all_id = []

    version = 5.101
    domain = "185219748"

    response = requests.get('https://api.vk.com/method/groups.getMembers',
                        params={'access_token': token_app,
                                'v': version,
                                'group_id': domain,
                                'count': 100})
    data = response.json()['response']['items']
    all_id.extend(data)
    #print(all_id)

    for i in all_id:
        vk_session.method('messages.send', {'user_id': i, 'message': message, 'random_id': 0})

