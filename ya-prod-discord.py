import discord
from discord import app_commands, ui
from discord.ext import commands
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

# Partie modal pour les commandes envoyer sur annonce
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

# Commande envoyer sur annonces avec restriction
@tree.command(name = "envoyer-une-annonce", description = "Faire un message dans Annonces")
@app_commands.describe(ping="Voulez-vous mentionner @everyone ?")
@app_commands.rename(ping='ping_everyone')
@app_commands.choices(ping=[
        app_commands.Choice(name="Oui", value=1),
        app_commands.Choice(name="Non", value=2)
    ])
async def react(interaction: discord.Interaction, ping : app_commands.Choice[int]):
    if  interaction.user.get_role(1007723429757194260):
        global chanid
        chanid = 1028728778890944613
        global reponse
        reponse = ping.value
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande envoyer sur interne avec restriction
@tree.command(name = "envoyer-une-annonce-interne", description = "Faire un message dans Annonces Interne")
@app_commands.describe(ping="Voulez-vous mentionner @everyone ?")
@app_commands.rename(ping='ping_everyone')
@app_commands.choices(ping=[
        app_commands.Choice(name="Oui", value=1),
        app_commands.Choice(name="Non", value=2)
    ])
async def react(interaction: discord.Interaction, ping : app_commands.Choice[int]):
    if  interaction.user.get_role(1007723429757194260):
        global chanid
        chanid = 1100114343758139483
        global reponse
        reponse = ping.value
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande Toolbox
@tree.command(name = "toolbox", description = "Donne l'url de la toolbox")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"*{interaction.user}* à demandé où était la toolbox. Elle se trouve sur https://yuanang.space/toolbox")

# Commande Demande
@tree.command(name = "demande", description = "Donne l'url pour introduire une demande")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"*{interaction.user}* à demandé où introduire une demande. Il faut aller sur https://yuanang.space/envoyer-ma-demande/")

# Commande howitwork
@tree.command(name = "howitwork", description = "Des infos pour les curieux")
async def react(interaction: discord.Interaction):
    await interaction.response.send_message(f"*{interaction.user}* petit curieux! Tu trouvera tout le code à cette adresse https://github.com/darktweek/bot-discord-ya")

# Commande de KICK
@tree.command(name = "kick", description = "Permet de Kick des Membres")
async def react(ctx, membre: discord.Member, raison: str):
    if  ctx.user.get_role(1007723429757194260):
        channel = client.get_channel(1130582595940388923)
        await ctx.guild.kick(membre)
        await channel.send(f'🧹 ← *{membre.name}* à été **kick** pour la raison: {raison}')
        await ctx.response.send_message(f"Tu à **kick** *{membre.name}*", ephemeral=True)
    else:
        await ctx.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande de BAN
@tree.command(name = "ban", description = "Permet de BAN des Membres")
async def react(ctx, membre: discord.Member, raison: str):
    if  ctx.user.get_role(1007723429757194260):
        channel = client.get_channel(1130582595940388923)
        await ctx.guild.ban(membre)
        await channel.send(f'💥 ← *{membre.name}* à été **ban** pour la raison: {raison}')
        await ctx.response.send_message(f"Tu à **ban** {membre.name}", ephemeral=True)
    else:
        await ctx.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# A la connection, envoyer un MP + message
@client.event
async def on_member_join(member):
    channel = client.get_channel(1130582595940388923)
    await channel.send(f"🎉 → *{member.name}*, c'est connecté au serveur Discord",)
    await member.create_dm()
    await member.dm_channel.send(
        f"Salutations {member.name},\nTu viens de rejoindre **{member.guild.name}** !\nJe t'invite à lire le <#1024248905925398558> et de faire la manipulation pour lier ton Handle à fin de pouvoir pleinement utiliser le serveur. \nSache que si tu n'a pas validé ton Handle, un kick sera automatiquement appliqué. \nA bien vite !")

# A la déconnection, envoyer message
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1130582595940388923)
    await channel.send(f"😞 ← *{member.name}*, c'est déconnecté du serveur Discord",)


@client.event
async def on_ready():
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN"))
