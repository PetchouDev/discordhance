import discord
from discord.ext import commands, tasks
from discord import app_commands

from core.config import MNGR
from core.decorators import custom_guilds


class Basics(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # local command example
    @app_commands.command(name="ping", description="Renvoie le ping du bot.")
    @custom_guilds([discord.Object(MNGR["guilds"][guild_name]["id"]) for guild_name in MNGR["guilds"]])
    async def ping(self, ctx: discord.Interaction):
        await ctx.response.send_message(f"Pong ! {round(self.bot.latency * 1000)}ms", ephemeral=True)

    # global command example
    @app_commands.command(name="message", description="Send message to user.")
    @app_commands.describe(
        user="L'utilisateur à qui envoyer le message.",
        msg="Le message à envoyer.",
        )
    async def message(self, ctx: discord.Interaction, user: discord.User, msg:str):
        try:
            await ctx.response.send_message("Message envoyé.", ephemeral=True)
        except:
            pass
        dest = await self.bot.fetch_user(user.id)
        await dest.send(msg if msg != "" else ":middle_finger:")

    # prefix command example
    @commands.command(name="ping", description="Send pong.")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong ! {round(self.bot.latency * 1000)}ms")

    # task example
    @tasks.loop(minutes=5)
    async def task_loop(self):
        print("Task loop")



