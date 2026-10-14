from getpass import getpass
from instagrapi import Client

def get_instagram_data():
    client = Client()

    username = input("Enter your Instagram username: ")
    password = getpass("Enter your Instagram password: ")

    client.login(username, password)
    user_id = client.user_id

    print("Fetching followers...")
    followers = client.user_followers(user_id)

    print("Fetching following...")
    following = client.user_following(user_id)

    return followers, following