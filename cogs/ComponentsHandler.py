from typing import Optional

import discord
from discord import Embed, app_commands, ButtonStyle, app_commands
from discord.ext import commands
from discord.ui import Button, View

from core.config import MNGR
from core.decorators import custom_guilds


class ComponentsHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # catch interaction events
    @commands.Cog.listener()
    async def on_interaction(self, ctx: discord.Interaction):
        
        if ctx.type == discord.InteractionType.component:            
            custom_id = ctx.data['custom_id']

            await ctx.response.defer()

            if custom_id == "ticket":
                
                ticket_created_embed = discord.Embed(
                    title="Demande de dossier",
                    description=f"""Hi {ctx.user.display_name}, your ticket has been opened.\nPlease describe your request in this channel.""",
                )
                
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                    ctx.user: discord.PermissionOverwrite(view_channel=True),
                    ctx.guild.me: discord.PermissionOverwrite(view_channel=True),
                    ctx.guild.get_role(MNGR["guilds"][ctx.guild.name]["moderator_role"]): discord.PermissionOverwrite(view_channel=True),
                }
                
                ticket = await ctx.guild.create_text_channel(
                    f"{ctx.user.name}-{ctx.user.id}", overwrites=overwrites, category=discord.utils.get(ctx.guild.categories, id=MNGR["guilds"][ctx.guild.name]["ticket_category"])
                )
                
                await ticket.send(
                    ctx.user.mention, embed=ticket_created_embed
                )  

    # create a button to open a ticket
    @app_commands.command(name="close", description="Create a button to open a ticket.")
    @custom_guilds([discord.Object(MNGR["guilds"][guild_name]["id"]) for guild_name in MNGR["guilds"]])
    @app_commands.checks.has_role([MNGR["guilds"][guild_name]["moderator_role"] for guild_name in MNGR["guilds"]])
    async def dossier(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title="Open a ticket",
            description="Click on the button below to open a ticket.",
        )
        btn = Button(label="🗃️ Open a ticket", custom_id="ticket", style=ButtonStyle.primary)

        # create a view and add the button
        view = View()
        view.add_item(btn)
        
        await ctx.channel.send(embed=embed, view=view)


    # other restricted command example, that close a ticket
    @app_commands.command(name="close", description="Close a ticket.")
    @custom_guilds([discord.Object(MNGR["guilds"][guild_name]["id"]) for guild_name in MNGR["guilds"]])
    @app_commands.checks.has_role([MNGR["guilds"][guild_name]["moderator_role"] for guild_name in MNGR["guilds"]])
    @app_commands.describe(comment="Comment to add to the closure message, facultative.")
    async def close(self, ctx: discord.Interaction, comment: Optional[str] = None):
        # check if the command is used in a ticket
        if not ctx.channel.category_id == MNGR["guilds"][ctx.guild.name]["ticket_category"]:
            await ctx.response.send_message("❌ This command can only be used in a ticket channel.", ephemeral=True)
            return
        
        # get the opener
        opener_id = int(ctx.channel.name.split("-")[1])
        opener = ctx.guild.get_member(opener_id)
        print(opener_id, opener)

        if opener is None:
            await ctx.user.send("❌ Coundn't find the ticker origin.", ephemeral=True)
            return

        # notify the opener
        embed = Embed(
            title="ticket closed",
            color=discord.Colour(0x9dec3c),
            description=f"Ticket closed by {ctx.user.mention}."
            )
        
        if comment is not None:
            embed.add_field(name="Comments", value=comment, inline=False)
        
        await opener.send(embed=embed)
        await ctx.user.send("✅ Ticket closed.")
        
        # delete the channel
        await ctx.channel.delete()

