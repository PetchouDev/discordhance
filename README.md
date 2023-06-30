# DISCORDENCE  V0.1.0
![Version](https://img.shields.io/badge/version-0.1.0-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54)
![Discord.py](https://img.shields.io/badge/discord.py-2.2.3-blue)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)
![MacOS](https://img.shields.io/badge/MacOS-000000?logo=apple&logoColor=white)


## Note:
This is a pre-release version. It is not recommended to use it in production.
If you find any bug, please report it in the issues section, and I will try to fix it as soon as possible.

## Table of content
- [DISCORDENCE](#discordence)
  - [Table of content](#table-of-content)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Setup](#setup)
    - [Commands](#commands)
    - [Tasks](#tasks)
    - [Events](#events)
    - [Dashboard integration](#dashboard-integration)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Introduction
Discordence is a discord bot template that is easy to use and easy to understand. It is written in python and uses the discord.py library. 
It comes with a few commands and a few events, even if they are more designed for example purposes than for actual use.

## Installation
1. Install python 3.8 or higher
2. Clone the repository with `git clone https://github.com/@PetchouDev/discordence`
3. Browse to the folder with `cd discordence`
4. Install the requirements with `pip install -r requirements.txt`


## Usage
### Setup
1. Create a bot application on the [discord developer portal](https://discord.com/developers/applications).
2. Copy the token and save it to your clipboard.
3. Run `python manage.py --setup` and paste the token when asked. You will be prompted for a password, this will be used to encrypt your token and make it unreadable if someone access your files (recommended) for more security.
4. Make sure  the process worked by simply checking if the token displayed in your terminal is the same as the one you copied earlier.
5. Edit the `data/data.json` file to your liking. You can change the prefix and the debug mode (0 = off, 1 = on - not implemented yet). You will also find how to manage guilds and their settings in this file. You don't have to use the same attributes, but keeping **ids** it strongly recommended.
6. **For large scale projects** json files can be a great start ing point, but they are not the best solution. A better solution would be to use a database, such as sqlite3 or mysql.

### Commands
You can either add commands directly to `core/client.py` (not recommended) or create a new file with a CoG class in it in the `cogs` folder. You can find an example already present in the folder, with examples of commands.

### Tasks
As for commands, you can either add events directly to `core/client.py` (not recommended) or create a new file with a CoG class in it in the `cogs` folder. 
To start a task, you must call it somehow **after** waking the bot up. An example is given is the `on_ready` event in `core/client.py`.

### Events
Once again, you can either add events directly to `core/client.py` (not recommended) or create a new file with a CoG class in it in the `cogs` folder. If you use events in CoGs, you must add the `@commands.Cog.listener()` decorator to the function. An example is given is the `cogs/ComponentsHandler.py` file.

### Dashboard integration
To use the bot with a custom dashboard, the best approach is to run a webserver in a separate thread (not implemented yet). You can instaciate the thread from the bot at in the `__init__` method, to pass the bot as attribute of the webserver and make all hsi attributes accessible. 
It is also recommended to listen only for `POST` requests with data at json format, and to use a secret key to make sure the requests are coming from the dashboard and not from somewhere else. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Contact
You can contact me on discord at @petchoudev or by email [here](mailto:contact@petchou.ovh)