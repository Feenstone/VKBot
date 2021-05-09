import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from toks import main_token
from vk_api.exceptions import ApiError

vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def get_group_by_id(group_id):
    group_info = vk_session.method("groups.getById", {'group_id': group_id, 'random_id': 0})
    return group_info


def sender(user_id, message_text):
    try:
        vk_session.method('messages.send', {'user_id': user_id, 'message': message_text, 'random_id': 0})
    except ApiError:
        print("Unable to send message to user with id: ", user_id)


group = get_group_by_id('public204339163')
message = input()
vk_users = vk_session.method("groups.getMembers", {'group_id': group[0]['id'], 'random_id': 0})

if message != "":
    for i in vk_users['items']:
        sender(i, message)
