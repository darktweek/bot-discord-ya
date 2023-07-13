import discord
from discord import app_commands, ui
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

class Message(ui.Modal, title='Message à envoyer sur Annonces'):
    titre = ui.TextInput(label="Titre de l'annonce")
    texte = ui.TextInput(label='Message', style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        global chanid
        channel = client.get_channel(chanid)
        embed = discord.Embed(title = f"{self.titre}", description = f"{self.texte}", color = 0x5865F2)
        embed.set_footer(text = f"Message de {interaction.user}")
        await interaction.response.send_message(f'{interaction.user}, ton message est envoyé sur <#{chanid}>', ephemeral=True)
        await channel.send(f"@everyone", embed = embed)

@tree.command(name = "send-to-annonces", description = "Faire un message dans Annonces")
async def react(interaction: discord.Interaction):
    if  interaction.user.get_role(1007723429757194260):
        global chanid
        chanid = 1028728778890944613   
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

@tree.command(name = "send-to-annonces-int", description = "Faire un message dans Annonces Interne")
async def react(interaction: discord.Interaction):
    if  interaction.user.get_role(1007723429757194260):
        global chanid
        chanid = 1100114343758139483   
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

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
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN"))
