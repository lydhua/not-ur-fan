def analyze_followers(followers, following):
    follower_ids = set(followers.keys())
    following_ids = set(following.keys())

    not_following_me_back = following_ids - follower_ids

    usernames = [
        following[user_id].username for user_id in not_following_me_back
    ]

    return sorted(usernames)