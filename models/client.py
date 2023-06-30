from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, token, *args, **kwargs):
        ...

    async def on_ready(self):
        ...

    def wake_up(self):
        ...

    def load_data(self):
        ...

    def save_data(self):
        ...

    async def load_module(self, module):
        ...

    def add_module(self, module):
        ...

    # start task from CoG
    def start_task(self, module: commands.Cog, task_name:str):
        ...

    # run a task from a CoG
    async def run_loop_asyncronously(self, module: commands.Cog, task_name:str):
            ...

    # sync the command tree with all guilds
    async def sync_all(self):
        ...


