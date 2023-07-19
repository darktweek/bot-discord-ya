import discord
from discord import app_commands, ui
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(name = "ban", description = "Permet de BAN des Membres")
async def react(ctx, membre: discord.Member, raison: str):
    if  ctx.user.get_role(1131271268415586434):
        channel = client.get_channel(1130508586926219275)
        await ctx.guild.ban(membre)
        await channel.send(f'💥 ← *{membre.name}* à été **ban** pour la raison: {raison}')
        await ctx.response.send_message(f"Tu à **ban** {membre.name}", ephemeral=True)
    else:
        await ctx.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)


@client.event
async def on_ready():
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN-DEV"))
