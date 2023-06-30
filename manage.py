import os

import discord

from core.client import Bot
from tools.crypto import load_flag_with_password, load_flag_without_password, test_password, setup
from tools.parser import parse_args

from core.config import MNGR, BASE_DIR

# import cogs
from cogs.ComponentsHandler import ComponentsHandler
from cogs.Basics import Basics


def run_bot(password=None):
    # check for token file existence
    exits = os.path.isfile(BASE_DIR / 'data' / 'token')

    if not exits:
        print("Token file not found. Run setup first.")
        exit(1)

    if MNGR["config"]["password"] == "yes":
        if password:
            bot = Bot(load_flag_with_password(password), intents=discord.Intents.all(), command_prefix="!")
        else:
            bot = Bot(load_flag_with_password(), intents=discord.Intents.all(), command_prefix="!")
    else:
        bot = Bot(load_flag_without_password(), intents=discord.Intents.all(), command_prefix="!")

    # add modules to the bot (at this point, they will be loaded by wake_up function, so no need to perform it manually)
    bot.add_module(ComponentsHandler)
    bot.add_module(Basics)

    bot.load_data()
    bot.wake_up()


def main():
    args = parse_args()

    # run setup
    if args.setup:
        setup()

    # run bot
    elif args.run:
        if args.password:
            run_bot(args.password[0])
    
        else:
            run_bot()

    # test password
    elif args.test:
        if args.password:
            test_password(args.password[0])

        else:
            test_password()

    # run bot by default
    else:
        if args.password:
            run_bot(args.password[0])
        else:
            run_bot()

if __name__ == "__main__":
    main()
