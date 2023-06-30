from typing import List, Union
from functools import wraps

from discord import Guild, Object, abc
from discord.ext.commands import check
from discord.ext import commands

def custom_guilds(guild_ids: List[Union[int, Guild, Object]]):
    def predicate(ctx):
        if not isinstance(ctx.guild, abc.GuildChannel):
            raise commands.NoPrivateMessage()
        
        if not ctx.guild.id in [g.id if isinstance(g, Guild) else g for g in guild_ids]:
            raise commands.CheckFailure(f"Not allowed in this guild.")
        
        return True

    return check(predicate)