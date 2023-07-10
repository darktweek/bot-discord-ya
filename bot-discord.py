import discord
from discord import app_commands, ui
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


class Message(ui.Modal, title='Message à envoyé sur Annonces'):
    texte = ui.TextInput(label='Message', style=discord.TextStyle.paragraph)
    
    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title = f"Annonce de {interaction.user}", description = f"{self.texte}")
        embed.set_author(name = interaction.user, icon_url=interaction.user.avatar)
        await interaction.response.send_message(f'{interaction.user}, ton message est envoyé', ephemeral=True)
        channel = client.get_channel(1028728778890944613)
        await channel.send(embed = embed)

@tree.command(name = "message-vers-annonces", description = "Faire un message dans Annonces")
async def react(interaction: discord.Interaction):
    await interaction.response.send_modal(Message())

@tree.command(name = "toolbox", description = "Donne l'url de la toolbox")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} à demandé où était la toolbox. Elle se trouve sur https://yuanang.space/toolbox")

@tree.command(name = "demande", description = "Donne l'url pour introduire une demande")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} à demandé où introduire une demande. Il faut aller sur https://yuanang.space/envoyer-ma-demande/")



@client.event
async def on_ready():
    #  Sync tree with discord.
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN"))
