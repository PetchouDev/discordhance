import asyncio

from discord.ext import commands

from core.config import MNGR


class Bot(commands.Bot):
    def __init__(self, token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.load_data()
        self.modules = []

    async def on_ready(self):

        # load modules
        if len(self.modules) == 0:
            pass
        else:
            for m in self.modules:
                await self.load_module(m)

        # sync the command tree with all guilds
        await self.sync_all()

        # start tasks
        self.start_task(self.get_cog("Basics"), "task_loop")
            

    def wake_up(self):
        self.run(self.token)

    def load_data(self):
        self.data = MNGR

    def save_data(self):
        self.data.save()

            
    async def load_module(self, module: commands.Cog):
        if module not in self.modules:
            self.modules.append(module)
        try:
            self.add_cog(module)
        except Exception as e:
            print(e)


    def add_module(self, module):
        if module not in self.modules:
            self.modules.append(module)
        else:
            pass

    # start task from CoG
    def start_task(self, module: commands.Cog, task_name:str):
        asyncio.run(self.run_loop_asyncronously(module, task_name))


    # run a task from a CoG
    async def run_loop_asyncronously(self, module: commands.Cog, task_name:str):
            await getattr(module, task_name).start()

    # sync the command tree with all guilds
    async def sync_all(self):
        for guild in self.guilds:
            await self.tree.sync(guild=guild)

        


    




