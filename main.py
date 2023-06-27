import discord, json
from discord.ext import commands, tasks
from datetime import datetime
import asyncio

with open('config.json', 'r') as f:
    config = json.load(f)
required_fields = ['token', 'guildID', 'staffroleID', 'mutedroleID', 'logchannelID', 'botStatus', 'botPrefix', 'botStatusMSG']
for field in required_fields:
    if field not in config:
        raise ValueError(f'[ERR] The config value {field} is missing!')
token = config['token']
guildID = config['guildID']
staffroleID = config['staffroleID']
mutedroleID = config['mutedroleID']
logchannelID = config['logchannelID']
botStatus = config['botStatus']
botPrefix = config['botPrefix']
botStatusMSG = config['botStatusMSG']
loggingchannel = client.get_channel(logchannelID)
mutedrole = guild.get_role(mutedroleID)
staffrole = guild.get_role(staffroleID)
dateandtime = datetime.now().strftime("%d/%m/%Y ✦ %H:%M:%S")

intents = discord.Intents().all()
client = commands.Bot(command_prefix=botPrefix, intents=intents, status=discord.Status.botStatus, activity=discord.Game(botStatusMSG))

@client.event
async def on_ready():
    guild = client.get_guild(guildID)
    print(f"+---------------------------------+\n|            MASKEDBOT            |\n|           v1.0.0 BETA           |\n| https://tcsmasked.maskednet.org |\n+---------------------------------+\n>>> BOT INFORMATION <<<\nUsername: {client.user.name}\nStatus: {botStatus}\nStatus MSG: {botStatusMSG}\nPrefix: {botPrefix}\n\n>>> SERVER INFORMATION <<<\nServer Name: {guild.name}\nMember Count: {guild.member_count}"\nServer Owner: {guild.owner}\nServer Region: {guild.region}\nServer Verification Level: {guild.verification_level}\nLogging Channel: {loggingchannel.name}\nMuted Role: {mutedrole.name}\nStaff Role: {staffrole.name}\n\nEverything below this line of text will be related to the bots advanced logging system.\n")
    embed = discord.Embed(title="{client.user.name} is now online! :green_circle:", colour=0x00ff33, timestamp=datetime.now())
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if reason is None:
        print(f"[KICK] Staff member {ctx.author} failed to give a reason!")
        embed = discord.Embed(title=":red_circle: Please enter a reason for your kick!", colour=0xff0000, timestamp=datetime.now())
            embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await ctx.send(embed=embed)
    embed2 = discord.Embed(title=f"{member} has been kicked!", colour=0x04ff00)
        embed2.add_field(name="Reason of Kick", value=reason, inline=True)
        embed2.add_field(name="Staff Member", value=ctx.author, inline=True)
        embed2.add_field(name="Time of Kick", value=dateandtime, inline=True)
        embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await ctx.send(embed=embed2, delete_after=3.5)
    embed3 = discord.Embed(title=f"{member} has been kicked!", colour=0x04ff00)
        embed3.add_field(name="Reason of Kick", value=reason, inline=True)
        embed3.add_field(name="Staff Member", value=ctx.author, inline=True)
        embed3.add_field(name="Time of Kick", value=dateandtime, inline=True)
        embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed3)
    print(f"[KICK] {member} has been kicked from {guild.name} by {ctx.author} for {reason}")
    embed4 = discord.Embed(title=f"You have been kicked from {guild.name}", colour=0x1100ff)
        embed4.add_field(name="Reason of Kick", value=reason, inline=True)
        embed4.add_field(name="Staff Member", value=ctx.author, inline=True)
        embed4.add_field(name="Time of Kick", value=dateandtime, inline=True)
        embed4.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await member.send(embed=embed4)
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if reason is None:
        print(f"[BAN] Staff member {ctx.author} failed to give a reason!")
        embed = discord.Embed(title=":red_circle: Please enter a reason for your ban!", colour=0xff0000, timestamp=datetime.now())
            embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await ctx.send(embed=embed, delete_after=3.5)
    embed2 = discord.Embed(title=f"{member} has been banned!", colour=0x04ff00)
        embed2.add_field(name="Reason of Ban", value=reason, inline=True)
        embed2.add_field(name="Length of Ban", value="Permenant", inline=True)
        embed2.add_field(name="Staff Member", value=ctx.author, inline=True)
        embed2.add_field(name="Time of Ban", value=dateandtime, inline=True)
        embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await ctx.send(embed=embed2, delete_after=3.5)
    embed3 = discord.Embed(title=f"{member} has been banned!", colour=0x04ff00)
        embed3.add_field(name="Reason of Ban", value=reason, inline=True)
        embed3.add_field(name="Length of Ban", value="Permenant", inline=True)
        embed3.add_field(name="Staff Member", value=ctx.author, inline=True)
        embed3.add_field(name="Time of Ban", value=dateandtime, inline=True)
        embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed3)
    print(f"[BAN] {member} has been banned from {guild.name} by {ctx.author} for {reason}")
    embed4 = discord.Embed(title=f"You have been banned from {guild.name}", colour=0x1100ff)
        embed4.add_field(name="Reason of Ban", value=reason, inline=True)
        embed4.add_field(name="Length of Ban", value="Permenant", inline=True)
        embed4.add_field(name="Staff Member", value=ctx.author, inline=True)
        embed4.add_field(name="Time of Ban", value=dateandtime, inline=True)
        embed4.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await member.send(embed=embed4)
    await member.ban(reason=reason)

@client.command(aliases=['purge'])
async def clear(ctx, amount=1):
    if amount is 1:
        print(f"[CLEAR] Staff member {ctx.author} failed to give an amount!")
        embed = discord.Embed(title=":red_circle: Please enter an amount to clear!", colour=0xff0000, timestamp=datetime.now())
            embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await ctx.send(embed=embed, delete_after=3.5)
    print(f"[CLEAR] Staff member {ctx.author} has cleared {amount} messages from {ctx.channel.name}.")
    embed2 = discord.Embed(title=f"Clearing {amount} messages...", colour=0x1100ff)
        embed2.add_field(name="Amount of Messages", value=f"{amount} Messages", inline=True)
        embed2.add_field(name="Channel", value={ctx.channel.name}, inline=True)
        embed2.add_field(name="Staff Member", value={ctx.author}, inline=True)
        embed2.add_field(name="Time of Clear", value=dateandtime, inline=True)
        embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await ctx.send(embed=embed2, delete_after=3.5)
    await asyncio.sleep(3.5)
    await ctx.channel.purge(limit=amount)
    embed3 = discord.Embed(title=f"{ctx.channel.name} has been cleared!", colour=0x1100ff)
        embed3.add_field(name="Amount of Messages", value=f"{amount} Messages", inline=True)
        embed3.add_field(name="Channel", value={ctx.channel.name}, inline=True)
        embed3.add_field(name="Staff Member", value={ctx.author}, inline=True)
        embed3.add_field(name="Time of Clear", value=dateandtime, inline=True)
        embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed3)

client.run(token)