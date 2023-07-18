import discord
from discord import app_commands, ui
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_member_join(member):
    channel = client.get_channel(1130508586926219275)
    await channel.send(f"🎉 → *{member.name}*, c'est connecté",)
    await member.create_dm()
    await member.dm_channel.send(
        f"Salutations {member.name},\nTu viens de rejoindre **{member.guild.name}** !\nJe t'invite à lire le <#1024248905925398558> et de faire la manipulation pour lier ton Handle à fin de pouvoir pleinement utiliser le serveur. \nSache que si tu n'a pas validé ton Handle, un kick sera automatiquement appliqué. \nA bien vite !")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1130508586926219275)
    await channel.send(f"😞 ← *{member.name}*, c'est déconnecté",)

@client.event
async def on_ready():
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN-DEV"))
