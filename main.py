import discord
from discord import message
import asyncio
from discord.ext import commands
import random

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    channel = client.get_channel(901400223895683112)
    await client.change_presence(activity=discord.Game(name="Segítek!"))
    await channel.send("Golerd sikeresen betöltve!")



@client.command()
@commands.has_role("Adminisztrátor" or "Moderátor")
async def ter10jail(ctx, member: discord.Member):
    embedVar = discord.Embed(title="Be lettél börtönözve! (10 percre)",
                             description="Ha igazságtalannak érzed a bebörtönzést, akkor bármikor jelentheted ezt a Fellebezés csatornán.",
                             )
    role = discord.utils.get(member.guild.roles, name="Bebörtönözve")
    role2 = discord.utils.get(member.guild.roles, name="Tag")
    channel = discord.utils.get(member.guild.channels, name="🔨-𝘈𝘥𝘮𝘪𝘯𝘪𝘴𝘻𝘵𝘳á𝘤𝘪ó")
    if role not in member.roles:
        await channel.send(f"{member} sikeresen bebörtönözve 10 percre.")
        await member.send(embed=embedVar)
        await member.add_roles(role)
        await member.remove_roles(role2)
        await asyncio.sleep(600)
        await member.remove_roles(role)
        await member.add_roles(role2)
    else:
        await channel.send(f"{member} már be van börtönözve.")


@client.command()
@commands.has_role("Adminisztrátor" or "Moderátor")
async def unjail(ctx, member: discord.Member):
    embedVar = discord.Embed(title="Kiszabadítottak a börtönödből!",
                             description="",
                             )
    role = discord.utils.get(member.guild.roles, name="Bebörtönözve")
    channel = discord.utils.get(member.guild.channels, name="🔨-𝘈𝘥𝘮𝘪𝘯𝘪𝘴𝘻𝘵𝘳á𝘤𝘪ó")
    role2 = discord.utils.get(member.guild.roles, name="Tag")
    if role in member.roles:
        await channel.send(f"{member}-t sikeresen kiszabadítottad börtönéből.")
        await member.remove_roles(role)
        await member.add_roles(role2)
        await member.send(embed=embedVar)
    else:
        await channel.send(f"{member} nincs bebörtönözve.")


@client.command()
@commands.has_role("Adminisztrátor" or "Moderátor")
async def jail(ctx, member: discord.Member):
    embedVar = discord.Embed(title="Be lettél börtönözve! (Addig amíg ki nem szabadítanak.)",
                             description="Ha igazságtalannak érzed a bebörtönzést, akkor bármikor jelentheted ezt a Fellebezés csatornán.",
                             )
    role2 = discord.utils.get(member.guild.roles, name="Tag")
    role = discord.utils.get(member.guild.roles, name="Bebörtönözve")
    channel = discord.utils.get(member.guild.channels, name="🔨-𝘈𝘥𝘮𝘪𝘯𝘪𝘴𝘻𝘵𝘳á𝘤𝘪ó")
    await channel.send(f"{member} mostantól addig lesz bebörtönözve, amíg valaki ki nem szabadítja.")
    await member.send(embed=embedVar)
    await member.add_roles(role)
    await member.remove_roles(role2)


@client.command()
@commands.has_role("Adminisztrátor")
async def clearmsg(ctx, amount=10000000000):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_role("Tag")
async def segitseg(ctx):
    author = ctx.message.author

    role2 = discord.utils.get(author.guild.roles, name="Segítség!")
    channel = discord.utils.get(author.guild.channels, name="🔨-𝘈𝘥𝘮𝘪𝘯𝘪𝘴𝘻𝘵𝘳á𝘤𝘪ó")


    embed2 = discord.Embed(title="Sikeres segítségkérés!",
                           description="Hamarosan a segítségedre fog sietni egy adminisztrációs tag, addig kérlek várj türelemmel!",
                           color=0x00ff00)


    await author.send(embed=embed2)
    await author.add_roles(role2)
    await channel.send(f"Ping: @Adminisztrátor @Moderátor | {author} segítséget kért!")



@client.command()
@commands.has_role("Segítség!")
async def csatbezar(ctx):
    author = ctx.message.author
    role2 = discord.utils.get(author.guild.roles, name="Segítség!")

    await author.remove_roles(role2)



@client.command()
@commands.has_role("Adminisztrátor" or "Moderátor")
async def pwrite(ctx, member: discord.Member, message):
    author = ctx.message.author
    channel = discord.utils.get(author.guild.channels, name="🔨-𝘈𝘥𝘮𝘪𝘯𝘪𝘴𝘻𝘵𝘳á𝘤𝘪ó")
    embed1 = discord.Embed(title=f"𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐳𝐭𝐫á𝐜𝐢ó𝐬 𝐭𝐚𝐠 - {author}",
                           description=f"{message}")
    await member.send(embed=embed1)
    await channel.send(f"Az üzenet sikeresen elküldve {member} nevű felhasználónak.")



@client.command()
@commands.has_role("Tag")
async def poszt(ctx):
    category = discord.utils.get(ctx.guild.categories, name="► Közösségi Portál")
    author = ctx.message.author
    rando = random.randint(1, 1000000000)
    await ctx.guild.create_text_channel(f'{author} posztja. Szám: {rando}', category=category, send_messages=False)
    embed = discord.Embed(title="Sikeres posztolás!", description="Használd a .valposzt parancsot az üzenetküldésekhez!", color=0x00ff00)

    await author.send(embed=embed)




@client.command()
@commands.has_role("Tag")
async def valposzt(ctx, member:discord.TextChannel, message):
    author = ctx.message.author
    embed2 = discord.Embed(title="Ez nem engedélyezett!", description="Ebbe a csatornába nem küldhetsz üzenetet.")
    embed = discord.Embed(title=f"{author} üzenete.", description=f"{message}")
    embed3 = discord.Embed(title=f'Üzenet sikeresen továbbítva a: "{member}" csatornába.')
    if member.name == "📜-𝐋𝐞í𝐫á𝐬":
        await author.send(embed=embed2)
    elif member.name == "𝐏𝐚𝐫𝐚𝐧𝐜𝐬𝐨𝐤":
        await author.send(embed=embed2)
    elif member.name == "📜-𝐏𝐚𝐫𝐚𝐧𝐜𝐬𝐨𝐤-𝐥𝐞í𝐫á𝐬𝐚":
        await author.send(embed=embed2)
    elif member.name == "🔨-𝘈𝘥𝘮𝘪𝘯𝘪𝘴𝘻𝘵𝘳á𝘤𝘪ó":
        await author.send(embed=embed2)
    elif member.name == "📞-𝐒𝐞𝐠í𝐭𝐬é𝐠":
        await author.send(embed=embed2)
    elif member.name == "fellebbezés":
        await author.send(embed=embed2)
    else:
        await member.send(embed=embed)
        await author.send(embed=embed3)

@client.command()
@commands.has_role("Tag")
async def jelentes(ctx, member:discord.Member, message):
    author = ctx.message.author
    channel = client.get_channel(901400223895683112)
    embed = discord.Embed(title="Sikeres jelentés!", description=f"Sikeresen jelentetted {member} nevű felhasználót a következő indokkal --> {message}")
    embed2 = discord.Embed(title="VIGYÁZAT, FELJELENTETTEK!", description=f"Indok --> {message}")
    await channel.send(f"Ping: @Adminisztrátor @Moderátor | {author} jelentette {member} nevű felhasználót a következő indokkal -->\n"
                       f"{message}")
    await author.send(embed=embed)
    await member.send(embed=embed2)


client.run('OTAxMTU5MTU4NjQ3MjMwNDc1.YXLz3g.0_0FU5eiM4WcMl75r3zDHE9mEZY')
