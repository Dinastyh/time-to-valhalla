import discord
from discord import Client
from discord.app_commands.tree import CommandTree
from loguru import logger
from dataclasses import dataclass, field
from client.server_info import ServerInfo

@dataclass
class Time_To_Valhalla:
    client: Client
    tree: CommandTree
    servers: dict[int, ServerInfo] = field(default_factory=dict)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

time_to_valhalla = Time_To_Valhalla(client, tree)

@client.event
async def on_ready():
    logger.info("Time_To_Valhalla is ready")

