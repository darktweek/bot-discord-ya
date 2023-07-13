import discord
from discord import app_commands, ui
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

class Message(ui.Modal, title='Message à envoyer sur Annonces'):
    texte = ui.TextInput(label='Message', style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title = f"Annonce de {interaction.user}", description = f"{self.texte}", color = 0x5865F2)
        embed.set_author(name = "Yu'ānang", icon_url='https://yuanang.space/wp-content/uploads/2023/07/logo_v2fondround.png')
        await interaction.response.send_message(f'{interaction.user}, ton message est envoyé', ephemeral=True)
        global chanid
        channel = client.get_channel(chanid)
        await channel.send(f"@everyone", embed = embed)

@tree.command(name = "send-to-annonces", description = "Faire un message dans Annonces")
async def react(interaction: discord.Interaction):
    global chanid
    chanid = 1128629326179483668   
    await interaction.response.send_modal(Message())

@tree.command(name = "send-to-annonces-int", description = "Faire un message dans Annonces Interne")
async def react(interaction: discord.Interaction):
    global chanid
    chanid = 1007053041943461982   
    await interaction.response.send_modal(Message())

@tree.command(name = "toolbox", description = "Donne l'url de la toolbox")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} à demandé où était la toolbox. Elle se trouve sur https://yuanang.space/toolbox")

@tree.command(name = "demande", description = "Donne l'url pour introduire une demande")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} à demandé où introduire une demande. Il faut aller sur https://yuanang.space/envoyer-ma-demande/")

@tree.command(name = "howitwork", description = "Des infos pour les curieux")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} petit curieux! Tu trouvera tout le code à cette adresse https://github.com/darktweek/bot-discord-ya")

@client.event
async def on_ready():
    #  Sync tree with discord.
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN"))
