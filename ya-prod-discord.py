import discord
from discord import app_commands, ui
from discord.ext import commands
import os
from dotenv import load_dotenv
import fnmatch
from conf.list import hello_list

load_dotenv()

# Définition des variables
intents = discord.Intents.default()
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# Définition des variables de rôles
role_agentgm = 1007723429757194260
role_handlé = 1126149657140133940

# Définition des variables de chan
chan_annonces = 1028728778890944613
chan_annonces_int = 1100114343758139483
chan_trackersc = 1007690884499918848
chan_absences = 1095056597442646118
chan_entréesortie = 1130582595940388923

# Partie modal pour les commandes envoyer sur annonce et Tracker
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

# Commande envoyer sur annonces avec restriction agentgm
@tree.command(name = "envoyer-une-annonce", description = "Faire un message dans Annonces")
@app_commands.describe(ping="Voulez-vous mentionner @everyone ?")
@app_commands.rename(ping='ping_everyone')
@app_commands.choices(ping=[
        app_commands.Choice(name="Oui", value=1),
        app_commands.Choice(name="Non", value=2)
    ])
async def react(interaction: discord.Interaction, ping : app_commands.Choice[int]):
    if  interaction.user.get_role(role_agentgm):
        global chanid
        chanid = chan_annonces
        global reponse
        reponse = ping.value
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande envoyer sur interne avec restriction agentgm
@tree.command(name = "envoyer-une-annonce-interne", description = "Faire un message dans Annonces Interne")
@app_commands.describe(ping="Voulez-vous mentionner @everyone ?")
@app_commands.rename(ping='ping_everyone')
@app_commands.choices(ping=[
        app_commands.Choice(name="Oui", value=1),
        app_commands.Choice(name="Non", value=2)
    ])
async def react(interaction: discord.Interaction, ping : app_commands.Choice[int]):
    if  interaction.user.get_role(role_agentgm):
        global chanid
        chanid = chan_annonces_int
        global reponse
        reponse = ping.value
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande envoyer sur tracker-sc avec restriction handlé
@tree.command(name = "envoyer-sur-tracker", description = "Envoyer une information sur le tracker-sc")
async def react(interaction: discord.Interaction):
    if  interaction.user.get_role(role_handlé):
        global chanid
        chanid = chan_trackersc
        global reponse
        reponse = 2
        await interaction.response.send_modal(Message())
    else:
        await interaction.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Partie modal pour la commande Message d'absence
class Absence(ui.Modal, title='Prévenez de votre absence'):
    date = ui.TextInput(label="Dates de votre absence" , style=discord.TextStyle.short)
    texte = ui.TextInput(label="Raison", style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        global chanid
        channel = client.get_channel(chanid)
        embed=discord.Embed(title=f"Absence de ***{interaction.user}***", color=0x7300ff)
        embed.add_field(name="Date", value=f"{self.date}", inline=False)
        embed.add_field(name="Raison", value=f"{self.texte}", inline=False)
        embed.set_footer(text=f"Message de {interaction.user}")
        await interaction.response.send_message(f'*{interaction.user}*, ton message est envoyé sur <#{chanid}>', ephemeral=True)
        await channel.send(embed = embed)

# Commande Message d'absence
@tree.command(name = "absence", description = "Prévenir de votre absence")
async def react(interaction: discord.Interaction):
    global chanid
    chanid = chan_absences
    await interaction.response.send_modal(Absence())

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

# Commande de KICK avec restriction agentgm
@tree.command(name = "kick", description = "Permet de Kick des Membres")
async def react(ctx, membre: discord.Member, raison: str):
    if  ctx.user.get_role(role_agentgm):
        channel = client.get_channel(chan_entréesortie)
        await ctx.guild.kick(membre)
        await channel.send(f'🧹 ← *{membre.name}* à été **kick** pour la raison: {raison}')
        await ctx.response.send_message(f"Tu à **kick** *{membre.name}*", ephemeral=True)
    else:
        await ctx.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# Commande de BAN avec restriction agentgm
@tree.command(name = "ban", description = "Permet de BAN des Membres")
async def react(ctx, membre: discord.Member, raison: str):
    if  ctx.user.get_role(role_agentgm):
        channel = client.get_channel(chan_entréesortie)
        await ctx.guild.ban(membre)
        await channel.send(f'💥 ← *{membre.name}* à été **ban** pour la raison: {raison}')
        await ctx.response.send_message(f"Tu à **ban** {membre.name}", ephemeral=True)
    else:
        await ctx.response.send_message(f"Tu n'a pas la permission d'utiliser cette commande", ephemeral=True)

# A la connection, envoyer un MP + message
@client.event
async def on_member_join(member):
    channel = client.get_channel(chan_entréesortie)
    await channel.send(f"🎉 → *{member.name}*, c'est connecté au serveur Discord",)
    await member.create_dm()
    await member.dm_channel.send(
        f"Salutations {member.name},\nTu viens de rejoindre **{member.guild.name}** !\nJe t'invite à lire <#1024248905925398558> et <#1136254213626798101>, pour ensuite faire la manipulation à fin de pouvoir pleinement utiliser le serveur. \nSache que si tu n'a pas validé ton entrée, un kick sera automatiquement appliqué. \nA bien vite !")

# A la déconnection, envoyer message
@client.event
async def on_member_remove(member):
    channel = client.get_channel(chan_entréesortie)
    await channel.send(f"😞 ← *{member.name}*, c'est déconnecté du serveur Discord",)

# Wave pour les messages du matin
@client.event 
async def on_message(message):
    test_str = message.content.lower()
    res = bool(list(filter(lambda x: fnmatch.fnmatch(test_str, x), hello_list)))
    if res == True:
        await message.add_reaction('👋')

@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='au plus profond de vos désires'))
    await tree.sync()
    print("Commands synced.")

client.run(os.getenv("TOKEN"))
