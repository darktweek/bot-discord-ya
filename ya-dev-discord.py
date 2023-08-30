import discord
from discord import app_commands, ui
from discord.ext import commands
from datetime import timedelta, datetime
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

role_a_avoir = 1131271268415586434

chan_salon1 = 1130508586926219275
chan_salon2 = 1131561714668806227
chan_général = 1122252457645449258

HACK_OPTIONS = [
   discord.SelectOption(label='Hacking', value='hack', description='did you experience someone hacking?'),
   discord.SelectOption(label='Harassment', value='harass', description='did someone harass you?'),
   discord.SelectOption(label='Discord ToS', value='tos', description='did you experience someone break the discord ToS in the server?'),
   discord.SelectOption(label='Support', value='sup', description='do you need support?')
]

class HackView(discord.ui.View):
    def __init__(self):
      super().__init__(timeout=100)
    @discord.ui.select(placeholder="Please select an option", options=HACK_OPTIONS, max_values=1)
    async def reply_select(self, interaction: discord.Interaction, select: discord.ui.Select):
      value = select.values[0]
      if value == 'hack':
         await interaction.response.send_message(f"You selected hack!")
      else:
         await interaction.response.send_message(f"You didn't select hack.")

@tree.command(name='test', description='test')
async def react(interaction: discord.Interaction):
   await interaction.response.send_message(f"I'm here to help you", view=HackView())


@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='au plus profond de vos désires'))
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN-DEV"))
