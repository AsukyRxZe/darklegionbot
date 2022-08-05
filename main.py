import discord
import asyncio
import logging
from discord.ext import commands
import random

client = commands.Bot(command_prefix="dl!")

f = open("rules.txt", "r")
rules = f.readlines()

filtered_words = ["ficken","Huhrensohn","huhrensohn","hundesohn","wichser","arschloch","kokain","afrizic","fick dich"]

images = [
    'https://i.imgur.com/JQGhevZ.jpg'
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS529rjq0QD0zNzDg9jxVZCyEHh-_Jmesxwch2vbPG1wg&s'
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM4w70M5xr5UHs-5T-JLABFMubAJ2I1ozkOOQAAzG-Ig&s'
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnNPExpfWuqJfKX36Vvf_6BKiwP_BE9byjXQ&usqp=CAU'
    'https://images.nordbayern.de/image/contentid/policy:1.12098071:1651661992/13-starwarsday-weekend.jpg?f=16%3A9&h=480&m=FIT&w=900&$p$f$h$m$w=7f0e281'
]


@client.event
async def on_ready():
    print("Bot ist Online")

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Du kannst das nicht tun")
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Bitte gebe deine Argumente an")
        await ctx.message.delete()
    else:
        raise error






@client.command(aliases=['regel'])
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount), 


@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "Kein Grund angegeben"):
  try:
    await member.send("Du wurdest von SWGC gekicked, weil:"+reason)
  except:
    await ctx.send("Der Benutzer hat seine DM´s geschlossen")

  await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "Kein Grund angegeben"):
        await ctx.send(member.name + " wurde von SWGC gebannt, weil:"+reason)
        await member.ban(reason=reason)

@client.command(aliases=['u'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

          await ctx.guild.unban(user)
          await ctx.send(member_name +" wurde entbannt!")
          return

    await ctx.send(member+" wurde nicht gefunden")


@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(994289972796461187)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " wurde gemuted")



@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def werist(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.red())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status)
    embed.add_field(name="Avatar", value=member.avatar)
    embed.add_field(name="Account Erstellung", value=member.created_at)
    embed.add_field(name="Serverbeitritt", value=member.joined_at)
    embed.add_field(name="Aktivität", value=member.activity)
    embed.add_field(name="Nickname", value=member.nick)
    embed.add_field(name="Server Name", value=member.guild)
    embed.add_field(name="@ Name", value=member.mention)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Angefordert von {ctx.author.name}")
    await ctx.send(embed=embed)



@client.command()
async def meme(ctx):
    embed = discord.Embed(color = discord.Colour.red())

    random_link = random.choice(images)
    
    embed.set_image(url = random_link)

    await ctx.send(embed = embed)

        




client.run("OTkzMTE0OTg3MTkzMTg0Mjc5.GL6GqM.1u4TMhbPoYS5AhpoCvikWN1kBccLhS0EE2YkWQ")
