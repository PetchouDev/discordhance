import os
import sys

import discord

from core.client import Bot
from tools.crypto import load_token_with_password, load_token_without_password, test_password, setup
from tools.parser import parse_args

from core.config import MNGR, BASE_DIR

# import cogs
from cogs.ComponentsHandler import ComponentsHandler
from cogs.Basics import Basics


def run_bot(password=None):
    # check for token file existence
    exits = os.path.isfile(BASE_DIR / 'data' / 'token')

    if not exits:
        print("Token file not found. Aborting.")
        print(f"Please run the following command to setup the bot before running it :")
        print(f"{sys.executable} {BASE_DIR / 'manage.py'} setup")
        exit(1)

    if MNGR["config"]["password"] == "yes":
        if password:
            bot = Bot(load_token_with_password(password), intents=discord.Intents.all(), command_prefix="!")
        else:
            bot = Bot(load_token_with_password(), intents=discord.Intents.all(), command_prefix="!")
    else:
        bot = Bot(load_token_without_password(), intents=discord.Intents.all(), command_prefix="!")

    # add modules to the bot (at this point, they will be loaded by wake_up function, so no need to perform it manually)
    bot.modules += [ComponentsHandler, Basics]

    bot.load_data()
    bot.wake_up()


def main():
    args = parse_args()

    # run setup
    if args.mode == 'setup':
        setup()

    # test password
    elif args.mode == 'test':
        if args.password:
            test_password(args.password[0])

        else:
            test_password()

    # run bot
    else:
        if args.password:
            run_bot(args.password[0])
    
        else:
            run_bot()


if __name__ == "__main__":
    main()
