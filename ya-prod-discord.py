import discord
from discord import app_commands, ui
import os
from dotenv import load_dotenv

load_dotenv()

# Définition des variables
intents = discord.Intents.default()
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# Partie modal pour les commandes send-to
class Message(ui.Modal, title='Message à envoyer'):
    titre = ui.TextInput(label="Titre du message")
    texte = ui.TextInput(label='Message', style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        global chanid
        channel = client.get_channel(chanid)
        embed = discord.Embed(title = f"{self.titre}", description = f"{self.texte}", color = 0x5865F2)
        embed.set_footer(text = f"Message de {interaction.user}")
        await interaction.response.send_message(f'{interaction.user}, ton message est envoyé sur <#{chanid}>', ephemeral=True)
        await channel.send(f"@everyone", embed = embed)

# Commande send-to avec restriction
@tree.command(name = "send-to-annonces", description = "Faire un message dans Annonces")
async def react(interaction: discord.Interaction):
    if  interaction.user.get_role(1007723429757194260):
        global chanid
        chanid = 1028728778890944613   
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande send-to avec restriction
@tree.command(name = "send-to-annonces-int", description = "Faire un message dans Annonces Interne")
async def react(interaction: discord.Interaction):
    if  interaction.user.get_role(1007723429757194260):
        global chanid
        chanid = 1100114343758139483   
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande Toolbox
@tree.command(name = "toolbox", description = "Donne l'url de la toolbox")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} à demandé où était la toolbox. Elle se trouve sur https://yuanang.space/toolbox")

# Commande Demande
@tree.command(name = "demande", description = "Donne l'url pour introduire une demande")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} à demandé où introduire une demande. Il faut aller sur https://yuanang.space/envoyer-ma-demande/")

# Commande howitwork
@tree.command(name = "howitwork", description = "Des infos pour les curieux")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user} petit curieux! Tu trouvera tout le code à cette adresse https://github.com/darktweek/bot-discord-ya")

# A la connection, envoyer un MP + message
@client.event
async def on_member_join(member):
    channel = client.get_channel(1130582595940388923)
    await channel.send(f"🎉 → *{member.name}*, c'est connecté",)
    await member.create_dm()
    await member.dm_channel.send(
        f"Salutations {member.name},\nTu viens de rejoindre **{member.guild.name}** !\nJe t'invite à lire le <#1024248905925398558> et de faire la manipulation pour lier ton Handle à fin de pouvoir pleinement utiliser le serveur. \nSache que si tu n'a pas validé ton Handle, un kick sera automatiquement appliqué. \nA bien vite !")

# A la déconnection, envoyer message
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1130582595940388923)
    await channel.send(f"😞 ← *{member.name}*, c'est déconnecté",)


@client.event
async def on_ready():
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN"))
