import discord
from discord import app_commands
from datetime import datetime
from loguru import logger
from client.client import time_to_valhalla
from client.server_info import ServerInfo

@time_to_valhalla.tree.command(name="select-channel", description="Select the \
                               current channel as bot annoncement channel")
@app_commands.checks.has_permissions(administrator = True)
@app_commands.checks.bot_has_permissions(send_messages=True)
@app_commands.checks.bot_has_permissions(view_channel=True)
async def select_channel(ctx: discord.Interaction):

    servers = time_to_valhalla.servers

    if not ctx.channel_id or not ctx.guild_id:
        await ctx.response.send_message("Fail to get current channel_id")
        logger.error("Fail to get current channel")
        return
    
    server_info = servers.get(ctx.channel_id) 

    if not server_info:
        servers[ctx.guild_id] = ServerInfo(ctx.guild_id, ctx.channel_id)
        logger.info(f"New server registered {ctx.guild_id}")
    else:
        server_info.channel = ctx.channel_id

    logger.info(f"Channel {ctx.channel_id} selected for {ctx.guild_id}")
    await ctx.response.send_message("Current channel selected")


@time_to_valhalla.tree.command(name="select-date", description="Choose the end date")
@app_commands.checks.has_permissions(administrator = True)
async def select_date(ctx: discord.Interaction, msg: str):

    servers = time_to_valhalla.servers

    if not ctx.channel_id or not ctx.guild_id:
        await ctx.response.send_message("Fail to get current channel_id")
        logger.error("Fail to get current channel")
        return

    server_info = servers.get(ctx.guild_id)

    if not server_info:
        await ctx.response.send_message("You must select\
        a channel before select a date")
        logger.error("Server not setup")
        return
    
    try:
        date = datetime.strptime(msg, '%d-%m-%Y')
    except Exception:
        await ctx.response.send_message(f"Error: {msg} not matching '%d-%m-%Y'")
        logger.error(f"Not matching date: {msg} in guild: {ctx.guild_id}")
        return

    server_info.date = date
    logger.info(f"Date selected: {date.date()}")
    await ctx.response.send_message(f"Date selected: {date.date()}")

