"""
    instabot example

    Workflow:
        If media is commented, reply to comments
        if you didn't reply yet to that user.
"""
from __future__ import unicode_literals

import argparse
import os
import sys
import time
from random import seed
from random import randint


from tqdm import tqdm, trange

sys.path.append(os.path.join(sys.path[0], "../../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("-link", type=str, help="media_link", required=True)
args = parser.parse_args()

if not args.link:
    print("You need to pass the media link with option\n" "-link MEDIA_LINK")
    exit()

bot = Bot()
bot.login(username=args.u, password=args.p, proxy=args.proxy)


bot.console_print("==============================================================================================================================================================", "orange")
bot.console_print("========================================================================  * SORTEO *  ========================================================================", "orange")
bot.console_print("==============================================================================================================================================================", "orange")
bot.console_print("Buscando comentarios...", "lpurple")

media_id = bot.get_media_id_from_link(args.link)
comments = bot.get_media_comments_all(media_id)
if len(comments) == 0:
    bot.logger.info("Media `{link}` has got no comments yet.".format(args.link))
    exit()

seed(1)
value = randint(0, len(comments)-1)

bot.console_print("Se encontraron " + str(len(comments)) + " comentarios", "lpurple")
bot.console_print("")
bot.console_print("Buscando ganadorx", "lpurple")

for comment in tqdm(range(0,100)):
    time.sleep(0.1)

bot.console_print("Ya tenemos ganadora", "lred")
bot.console_print("3", "lred")
time.sleep(1)
bot.console_print("2", "lred")
time.sleep(1)
bot.console_print("1", "lred")
time.sleep(1)

bot.console_print("Gano "+str(comments[value]["user"]["username"]), "lpurple")
bot.console_print("Felicitaciones!!!", "lpurple")
bot.console_print("")
bot.console_print("")
bot.console_print("")