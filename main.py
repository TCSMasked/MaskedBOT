import discord, json, re, asyncio
from discord.ext import commands, tasks
from datetime import datetime

with open('config.json', 'r') as f:
    config = json.load(f)
required_fields = ['token', 'welcomeFeature', 'goodbyeFeature', 'badWordDetector', 'serverInvitesDetector', 'AntiSpam', 'guildID', 'staffroleID', 'mutedroleID', 'logchannelID', 'botStatus', 'botPrefix', 'botStatusMSG']
for field in required_fields:
    if field not in config:
        raise ValueError(f'[ERR] The config field {field} is missing!')
token = config['token']
guildID = config['guildID']
staffroleID = config['staffroleID']
mutedroleID = config['mutedroleID']
logchannelID = config['logchannelID']
botStatus = config['botStatus']
botPrefix = config['botPrefix']
botStatusMSG = config['botStatusMSG']
badWordDetectorOption = config['badWordDetector']
serverInvitesDetectorOption = config['serverInvitesDetector']
AntiSpamOption = config['AntiSpam']
welcomeFeatureOption = config['welcomeFeature']
welcomeFeatureChannelID = config['welcomeFeatureChannelID']
goodbyeFeatureOption = config['goodbyeFeature']
goodbyeFeatureChannelID = config['goodbyeFeatureChannelID']
goodbyeChannel = client.get_channel(goodbyeFeatureChannelID)
welcomeChannel = client.get_channel(welcomeFeatureChannelID)
loggingchannel = client.get_channel(logchannelID)
mutedrole = guild.get_role(mutedroleID)
staffrole = guild.get_role(staffroleID)
dateandtime = datetime.now().strftime("%d/%m/%Y ✦ %H:%M:%S")
invite_links = ['discord.gg', 'discord.com/invite']
bad_words = ['nigger', 'nigga', 'faggot', 'fag', 'dike', 'queer']
variation_patterns = [
    r'([b4]+[^\w\s]*[a4]+[^\w\s]*[d]+[^\w\s]*[w]+[^\w\s]*[o0]+[^\w\s]*[r]+[^\w\s]*[d]+)',
    r'([f]+[^\w\s]*[u]+[^\w\s]*[c]+[^\w\s]*[k]+)',
    r'([s]+[^\w\s]*[h]+[^\w\s]*[i]+[^\w\s]*[t]+)'
]

intents = discord.Intents().all()
client = commands.Bot(command_prefix=botPrefix, intents=intents, status=discord.Status.botStatus, activity=discord.Game(botStatusMSG))

def contains_bad_word(message):
    content = message.content.lower()
    for word in bad_words:
        if word in content:
            return True
    for pattern in variation_patterns:
        if re.search(pattern, content):
            return True
    return False

@client.event
async def on_ready():
    guild = client.get_guild(guildID)
    print(f"+---------------------------------+\n|            MASKEDBOT            |\n|           v1.0.0 BETA           |\n| https://tcsmasked.maskednet.org |\n+---------------------------------+\n>>> BOT INFORMATION <<<\nUsername: {client.user.name}\nStatus: {botStatus}\nStatus MSG: {botStatusMSG}\nPrefix: {botPrefix}\n\n>>> SERVER INFORMATION <<<\nServer Name: {guild.name}\nMember Count: {guild.member_count}\nServer Owner: {guild.owner}\nServer Region: {guild.region}\nServer Verification Level: {guild.verification_level}\nLogging Channel: {loggingchannel.name}\nMuted Role: {mutedrole.name}\nStaff Role: {staffrole.name}\n\nEverything below this line of text will be related to the bots advanced logging system.\n")
    embed = discord.Embed(title="{client.user.name} is now online! :green_circle:", colour=0x00ff33, timestamp=datetime.now())
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if badWordDetectorOption is true:
        if contains_bad_word(message):
            await message.delete()
            embed = discord.Embed(title="Bad Word Detector", description="{message.author.display_name} sent a bad word!", colour=0xff0000, timestamp=datetime.now())
            embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
            await message.loggingchannel.send(embed=embed2)
    if serverInvitesDetectorOption is true:
        for link in invite_links:
            if link in content:
                await message.delete()
                embed2 = discord.Embed(title="Invite Link Detected", description="{message.author.display_name} sent a Discord Invite Link.", colour=0xff0000, timestamp=datetime.now())
                embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
                await message.loggingchannel.send(embed=embed2)
                break
    if AntiSpamOption is true:
        spam_counter = 0
        async for past_message in message.channel.history(limit=spam_threshold):
            if past_message.author == message.author:
                spam_counter += 1
        if spam_counter >= spam_threshold:
            await message.delete()
            embed3 = discord.Embed(title="AntiSpam", description="Spamming has been detected by {message.author.display_name}", colour=0xff0000, timestamp=datetime.now())
            embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
            await message.loggingchannel.send(embed=embed3)
    await client.process_commands(message)

@client.event
async def on_member_update(before, after):
    if before.nick != after.nick:
        embed = discord.Embed(title="Logging System  ✦  Nickname Changed", colour=0xff0000)
        embed.add_field(name="Member", value=after.mention, inline=True)
        embed.add_field(name="Name Before", value=before.display_name, inline=True)
        embed.add_field(name="Name After", value=after.display_name, inline=True)
        embed.add_field(name="Time of Change",value=dateandtime, inline=True)
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        embed.set_thumbnail(url=after.avatar_url)
        await loggingchannel.send(embed=embed)

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Logging System  ✦  Member Joined", colour=0xff0000)
    embed.add_field(name="Member", value=member.mention, inline=True)
    embed.add_field(name="User ID", value=member.id, inline=True)
    embed.add_field(name="Time of Join", value=dateandtime, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)
    if welcomeFeatureOption is true:
        embed2 = discord.Embed(title=f"Welcome to server, {member.display_name}", colour=0x44ff00, timestamp=datetime.now())
        embed2.set_thumbnail(url="member.avatar_url")
        embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await welcomeChannel.send(embed=embed2)

@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="Logging System  ✦  Member Left", colour=0xff0000)
    embed.add_field(name="Member", value=member.mention, inline=True)
    embed.add_field(name="User ID", value=member.id, inline=True)
    embed.add_field(name="Time of Leave", value=dateandtime, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)
    if goodbyeFeatureOption is true:
        embed2 = discord.Embed(title=f"{member.display_name} has left. :pleading_face:", colour=0xff0000, timestamp=datetime.now())
        embed2.set_thumbnail(url="member.avatar_url")
        embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await welcomeChannel.send(embed=embed2)

@client.event
async def on_guild_role_create(role):
    embed = discord.Embed(title="Logging System  ✦  Role Created", colour=0xff0000)
    embed.add_field(name="Role Name", value=role.name, inline=True)
    embed.add_field(name="Role ID", value=role.id, inline=True)
    embed.add_field(name="Time of Creation", value=dateandtime, inline=True)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)

@client.event
async def on_guild_role_update(before, after):
    if before.name != after.name:
        embed = discord.Embed(title="Logging System  ✦  Role Changed", colour=0xff0000)
        embed.add_field(name="Name Before", value=before.name, inline=True)
        embed.add_field(name="Name After", value=after.name, inline=True)
        embed.add_field(name="Role ID", value=role.id, inline=True)
        embed.add_field(name="Time of Creation", value=dateandtime, inline=True)
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await loggingchannel.send(embed=embed)

@client.event
async def on_guild_role_delete(role):
    embed = discord.Embed(title="Logging System  ✦  Role Deleted", colour=0xff0000)
    embed.add_field(name="Role Name", value=role.name, inline=True)
    embed.add_field(name="Role ID", value=role.id, inline=True)
    embed.add_field(name="Time of Deletion", value=dateandtime, inline=True)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)

@client.event
async def on_member_update_roles(member, before, after):
    added_roles = set(after) - set(before)
    removed_roles = set(before) - set(after)
    if added_roles:
        role_names = ', '.join([role.name for role in added_roles])
        embed = discord.Embed(title="Logging System  ✦  Role Added", colour=0xff0000)
        embed.add_field(name="Member", value=member.mention, inline=True)
        embed.add_field(name="Roles Added", value=role_names, inline=True)
        embed.add_field(name="Time of Event", value=dateandtime, inline=True)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await loggingchannel.send(embed=embed)
    if removed_roles:
        role_names = ', '.join([role.name for role in removed_roles])
        embed2 = discord.Embed(title="Logging System  ✦  Role Removed", colour=0xff0000)
        embed2.add_field(name="Member", value=member.mention, inline=True)
        embed2.add_field(name="Roles Removed", value=role_names, inline=True)
        embed2.add_field(name="Time of Event", value=dateandtime, inline=True)
        embed2.set_thumbnail(url=member.avatar_url)
        embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await loggingchannel.send(embed=embed2)

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel:
            embed = discord.Embed(title="Logging System  ✦  Joined VC", colour=0xff0000)
            embed.add_field(name="Member", value=member.mention, inline=True)
            embed.add_field(name="Channel", value=after.channel.name, inline=True)
            embed.add_field(name="Time of Join", value=dateandtime, inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
            await loggingchannel.send(embed=embed)
        else:
            embed2 = discord.Embed(title="Logging System  ✦  Left VC", colour=0xff0000)
            embed2.add_field(name="Member", value=member.mention, inline=True)
            embed2.add_field(name="Channel", value=before.channel.name, inline=True)
            embed2.add_field(name="Time of Leave", value=dateandtime, inline=True)
            embed2.set_thumbnail(url=member.avatar_url)
            embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
            await loggingchannel.send(embed=embed2)

@client.event
async def on_guild_channel_create(channel):
    embed = discord.Embed(title="Logging System  ✦  Channel Created", colour=0xff0000)
    embed.add_field(name="Channel Name", value=channel.name, inline=True)
    embed.add_field(name="Channel ID", value=channel.id, inline=True)
    embed.add_field(name="Time of Creation", value=dateandtime, inline=True)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)

@client.event
async def on_guild_channel_update(before, after):
    if before.name != after.name:
        embed = discord.Embed(title="Logging System  ✦  Channel Changed", colour=0xff0000)
        embed.add_field(name="Name Before", value=before.name, inline=True)
        embed.add_field(name="Name After", value=after.name, inline=True)
        embed.add_field(name="Channel ID", value=before.id, inline=True)
        embed.add_field(name="Time of Change", value=dateandtime, inline=True)
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await loggingchannel.send(embed=embed)

@client.event
async def on_guild_channel_delete(channel):
    embed = discord.Embed(title="Logging System  ✦  Channel Deleted", colour=0xff0000)
    embed.add_field(name="Channel Name", value=channel.name, inline=True)
    embed.add_field(name="Channel ID", value=channel.id, inline=True)
    embed.add_field(name="Time of Deletion", value=dateandtime, inline=True)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)

@client.event
async def on_message_delete(message):
    embed = discord.Embed(title="Logging System  ✦  Message Deleted", colour=0xff0000)
    embed.add_field(name="Member", value=message.author.mention, inline=True)
    embed.add_field(name="Message", value=message.content, inline=True)
    embed.add_field(name="Time of Deletion", value=dateandtime, inline=True)
    embed.set_thumbnail(url=message.author.avatar_url)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)

@client.event
async def on_message_edit(before, after):
    if before.content != after.content:
        embed = discord.Embed(title="Logging System  ✦  Message Edited", colour=0xff0000)
        embed.add_field(name="Member", value=before.author.mention, inline=True)
        embed.add_field(name="Message Before", value=before.content, inline=True)
        embed.add_field(name="Message After", value=after.content, inline=True)
        embed.add_field(name="Time of Deletion", value=dateandtime, inline=True)
        embed.set_thumbnail(url=before.author.avatar_url)
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await loggingchannel.send(embed=embed)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if reason is None:
        print(f"[KICK] Staff member {ctx.author.display_name} failed to give a reason!")
        embed = discord.Embed(title=":red_circle: Please enter a reason for your kick!", colour=0xff0000, timestamp=datetime.now())
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await ctx.send(embed=embed, delete_after=3.5)
    embed2 = discord.Embed(title=f"{member} has been kicked!", colour=0x04ff00)
    embed2.add_field(name="Reason of Kick", value=reason, inline=True)
    embed2.add_field(name="Staff Member", value=ctx.author.mention, inline=True)
    embed2.add_field(name="Time of Kick", value=dateandtime, inline=True)
    embed2.set_thumbnail(url=member.avatar_url)
    embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await ctx.send(embed=embed2, delete_after=3.5)
    embed3 = discord.Embed(title=f"Logging System  ✦  Member Kicked", colour=0x04ff00)
    embed3.add_field(name="Member", value=member.mention, inline=True)
    embed3.add_field(name="Reason of Kick", value=reason, inline=True)
    embed3.add_field(name="Staff Member", value=ctx.author, inline=True)
    embed3.add_field(name="Time of Kick", value=dateandtime, inline=True)
    embed3.set_thumbnail(url=member.avatar_url)
    embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed3)
    print(f"[KICK] {member.display_name} has been kicked from {guild.name} by {ctx.author.display_name} for {reason}")
    embed4 = discord.Embed(title=f"You have been kicked from {guild.name}", colour=0x1100ff)
    embed4.add_field(name="Reason of Kick", value=reason, inline=True)
    embed4.add_field(name="Staff Member", value=ctx.author, inline=True)
    embed4.add_field(name="Time of Kick", value=dateandtime, inline=True)
    embed4.set_thumbnail(url=member.avatar_url)
    embed4.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await member.send(embed=embed4)
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if reason is None:
        print(f"[BAN] Staff member {ctx.author.display_name} failed to give a reason!")
        embed = discord.Embed(title=":red_circle: Please enter a reason for your ban!", colour=0xff0000, timestamp=datetime.now())
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await ctx.send(embed=embed, delete_after=3.5)
    embed2 = discord.Embed(title=f"{member.mention} has been banned!", colour=0x04ff00)
    embed2.add_field(name="Reason of Ban", value=reason, inline=True)
    embed2.add_field(name="Length of Ban", value="Permenant", inline=True)
    embed2.add_field(name="Staff Member", value=ctx.author.mention, inline=True)
    embed2.add_field(name="Time of Ban", value=dateandtime, inline=True)
    embed2.set_thumbnail(url=member.avatar_url)
    embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await ctx.send(embed=embed2, delete_after=3.5)
    embed3 = discord.Embed(title=f"Logging System  ✦  Member Banned", colour=0x04ff00)
    embed3.add_field(name="Member", value=member.mention, inline=True)
    embed3.add_field(name="Reason of Ban", value=reason, inline=True)
    embed3.add_field(name="Length of Ban", value="Permenant", inline=True)
    embed3.add_field(name="Staff Member", value=ctx.author.mention, inline=True)
    embed3.add_field(name="Time of Ban", value=dateandtime, inline=True)
    embed3.set_thumbnail(url=member.avatar_url)
    embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed3)
    print(f"[BAN] {member.display_name} has been banned from {guild.name} by {ctx.author.display_name} for {reason}")
    embed4 = discord.Embed(title=f"You have been banned from {guild.name}", colour=0x1100ff)
    embed4.add_field(name="Reason of Ban", value=reason, inline=True)
    embed4.add_field(name="Length of Ban", value="Permenant", inline=True)
    embed4.add_field(name="Staff Member", value=ctx.author.display_name, inline=True)
    embed4.add_field(name="Time of Ban", value=dateandtime, inline=True)
    embed4.set_thumbnail(url=member.avatar_url)
    embed4.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await member.send(embed=embed4)
    await member.ban(reason=reason)

@client.command(aliases=['purge'])
async def clear(ctx, amount=1):
    if amount is 1:
        print(f"[CLEAR] Staff member {ctx.author.display_name} failed to give an amount!")
        embed = discord.Embed(title=":red_circle: Please enter an amount to clear!", colour=0xff0000, timestamp=datetime.now())
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await ctx.send(embed=embed, delete_after=3.5)
    print(f"[CLEAR] Staff member {ctx.author.display_name} has cleared {amount} messages from {ctx.channel.name}.")
    embed2 = discord.Embed(title=f"Clearing {amount} messages...", colour=0x1100ff)
    embed2.add_field(name="Channel", value={ctx.channel.name}, inline=True)
    embed2.add_field(name="Amount of Messages", value=f"{amount} Messages", inline=True)
    embed2.add_field(name="Staff Member", value={ctx.author.mention}, inline=True)
    embed2.add_field(name="Time of Clear", value=dateandtime, inline=True)
    embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await ctx.send(embed=embed2, delete_after=3.5)
    await asyncio.sleep(3.5)
    await ctx.channel.purge(limit=amount)
    embed3 = discord.Embed(title=f"Logging System  ✦  Channel Cleared", colour=0x1100ff)
    embed3.add_field(name="Channel", value={ctx.channel.name}, inline=True)
    embed3.add_field(name="Amount of Messages", value=f"{amount} Messages", inline=True)
    embed3.add_field(name="Staff Member", value={ctx.author.mention}, inline=True)
    embed3.add_field(name="Time of Clear", value=dateandtime, inline=True)
    embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed3)

@client.command()
async def warn(ctx, member : discord.Member, *, reason=None):
    if reason is None:
        print(f"[WARN] Staff member {ctx.author.display_name} failed to give a reason!")
        embed = discord.Embed(title=":red_circle: Please enter a reason for your warn!", colour=0xff0000, timestamp=datetime.now())
        embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
        await ctx.send(embed=embed, delete_after=3.5)
    embed = discord.Embed(title="Logging System  ✦  Member Warned", colour=0xff0000)
    embed.add_field(name="Member", value=member.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    embed.add_field(name="Staff Member", value=ctx.author.mention, inline=True)
    embed.add_field(name="Time of Warn", value=dateandtime, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await loggingchannel.send(embed=embed)
    embed2 = discord.Embed(title=f"{member.mention} has been warned!", colour=0xff0000)
    embed2.add_field(name="Reason", value=reason, inline=True)
    embed2.add_field(name="Staff Member", value=ctx.author.mention, inline=True)
    embed2.add_field(name="Time of Warn", value=dateandtime, inline=True)
    embed2.set_thumbnail(url=member.avatar_url)
    embed2.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await ctx.send(embed=embed2, delete_after=3.5)
    embed3 = discord.Embed(title=f"You have been warned in {guild.name}", colour=0xff0000)
    embed3.add_field(name="Reason", value=reason, inline=True)
    embed3.add_field(name="Staff Member", value=ctx.author.mention, inline=True)
    embed3.add_field(name="Time of Warn", value=dateandtime, inline=True)
    embed3.set_thumbnail(url=member.avatar_url)
    embed3.set_footer(text="Developed by TCSMasked", icon_url="https://tcsmasked.maskednet.org/tcsmasked.jpg")
    await member.send(embed=embed3)

client.run(token)