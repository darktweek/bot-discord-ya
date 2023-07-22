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


# Partie modal pour les commandes send-to
class Message(ui.Modal, title='Message à envoyer'):
    titre = ui.TextInput(label="Titre du message")
    texte = ui.TextInput(label='Message', style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        global chanid
        global reponse
        channel = client.get_channel(chanid)
        embed = discord.Embed(title = f"{self.titre}", description = f"{self.texte}", color = 0x5865F2)
        embed.set_footer(text = f"Message de *{interaction.user}*")
        await interaction.response.send_message(f'*{interaction.user}*, ton message est envoyé sur <#{chanid}>', ephemeral=True)
        if reponse == 1:
            await channel.send(f"@everyone", embed = embed)
        else:
            await channel.send(embed = embed)

# Commande send-to avec restriction
@tree.command(name = "envoyer-une-info", description = "Envoyer une info dans le tracker")
@app_commands.describe(ping="Voulez-vous mentionner @everyone ?")
@app_commands.rename(ping='ping_everyone')
@app_commands.choices(ping=[
        app_commands.Choice(name="Oui", value=1),
        app_commands.Choice(name="Non", value=2)
    ])
async def react(interaction: discord.Interaction, ping : app_commands.Choice[int]):
    if  interaction.user.get_role(1131271268415586434):
        global chanid
        global reponse
        chanid = 1131561714668806227   
        reponse = ping.value
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

@client.event
async def on_ready():
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN-DEV"))
