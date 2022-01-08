import vk
import getpass


APP_ID = 6934498
API_VERSION = '5.92'


def get_user_login():
    return input('User login: ')


def get_user_password():
    return getpass.getpass(prompt='User password: ')


def get_online_friends(login, password, api_version):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends'
        )
        api = vk.API(session, v=api_version)
        friends_online_ids = api.friends.getOnline()
        friends_online = api.users.get(user_ids=friends_online_ids)
    except vk.exceptions.VkAuthError:
        friends_online = None
    return friends_online


def output_friends_to_console(friends_online):
    if friends_online:
        for friend in friends_online:
            print('{} {}'.format(friend['last_name'], friend['first_name']))
    else:
        print('No friends online')


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password, API_VERSION)
    if friends_online is None:
        exit('Vk Authorization Error')
    output_friends_to_console(friends_online)
