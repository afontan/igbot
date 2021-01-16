"""
    instabot example

    Workflow:
        Follow user's followers by username.
"""

import argparse
import os
import sys
import random
import time

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
args = parser.parse_args()
bot = Bot(
    filter_users=True,
    filter_private_users=False,
    filter_previously_followed=True,
    filter_business_accounts=True,
    filter_verified_accounts=True,
    max_followers_to_follow=1000000,
    max_following_to_follow=200000,
    follow_delay=1,
    max_follows_per_day=100000,
    max_comments_per_day=10000
)
bot.login(username=args.u, password=args.p, proxy=args.proxy)

media_id = bot.get_media_id_from_link("https://www.instagram.com/p/CJmd49VgYT7/?igshid=13g2yiy5zex8o")

user_id = bot.get_user_id_from_username("lu__psiloveu")

following = bot.get_user_following(user_id)

for i in range(0, 1000):
    index = random.randint(0, len(following)-1)
    username = bot.get_username_from_user_id(following[index])
    bot.comment(media_id, '@'+username)
    print("Comment "+str(i)+": "+"@"+username)
    time.sleep(10)

#for username in args.users:
    #bot.follow_followers(username)
