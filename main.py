import discord
from discord.ext import commands
import os

import time
import random
from datetime import datetime

import json




# discord settings
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='/', intents=intents)





searchloc = [
  "kitchen!",
  "couch!",
  "living room!",
  "basement!",
  "closet!",
  "pillow case!",
  "bedroom!",
  "mom!",
  "tv!",
  "drawer!",
  "dad!",
  "toilet!",
  "cheeseburger!",
  "laptop!",
  "computer!",
  "chair!",
  "keyboard!",
  "mouse!",
  "monitor!",
  "phone!",
  "cat!",
  "dog!",
  "rat!",
  "brother!",
  "sister!",
  "dad's bedroom!",
  "mom's bedroom!",
  "mattress!"
]
# locations for command !search



# runs when bot starts
@client.event
async def on_ready():
    for guild in client.guilds:
      print(f"\n------------------{guild.name}------------------")

      # creating database
      try:
        with open(f"{guild.id}.json","r"):
          print("database already made.")
      except:
        print("we need to make a db")
        with open(f"{guild.id}.json","a") as file:
          file.write("{}")




      # adding users to database
      with open( f"{guild.id}.json" , 'r' ) as file:
        database = json.load(file)

      with open( f"{guild.id}.json" , 'a' ) as file:
        for user in guild.members:
          print(user.name)  
          if user.name in database:
            print("true")
          else:
            print('false')
            database[user.name] = 'yooo!'

          # dumb jason into the database
        print(database)



      found = False
      for x in range(0, len(guild.channels),1):
        if "join-log" in guild.channels[x].name :
          found = True
      if found:
        print("Already There!")
      else:
        print("He needs some sauce!")
        await guild.create_text_channel('join-log')
    
      




    

@client.event
async def on_guild_join(guild):
    print("joined... " + str(guild.id))

@client.event
async def on_guild_remove(guild):
    print("left... " + str(guild.id))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('almond is good'):
        await message.channel.send('Yes it is best.')
        # Secret Command.

    if message.content.startswith('what is sugondese'):
        await message.channel.send('you fell for it.')
        # Secret Command     

    if message.content.startswith('Almond is good'):
        await message.channel.send('Yes it is best.')
        # Secret Command.

    if message.content.startswith('/coinflip'):
        x = random.randint(1, 2)
        
        if str(x) == '1':
          await message.channel.send('Heads!')

        if str(x) == '2':
          await message.channel.send('Tails!') 
        # flips a coin

    if message.content.startswith('/setup'):
        await message.channel.send('')
        # Setup roles and channels.

    if message.content.startswith('/findjob'):
        await message.channel.send('Not Avalible yet.')
        # Looks for job.





    if message.content.startswith('/help'):
      embed=discord.Embed()
      embed.add_field(name="Music Commands", value="!music", inline=True)
      embed.add_field(name="Economy Commands", value="!eco", inline=False)
      embed.add_field(name="General Commands", value="!general", inline=False)
      embed.add_field(name="Administrator Commands", value="!adminc", inline=False)
      await message.channel.send(embed=embed)
      # Lists all commands.


    if message.content.startswith('/music'):
      embed=discord.Embed(title=" ")
      embed.set_author(name="Music Commands")
      embed.add_field(name="!play", value="Plays a certain song", inline=True)
      embed.add_field(name="!skip", value="Skips a song", inline=True)
      embed.add_field(name="!voteskip", value="Votes to skip a song", inline=True)
      embed.add_field(name="!queue", value="Shows current song queue", inline=True)
      embed.add_field(name="!dj", value='Gives a user "DJ" role to play songs', inline=True)
      embed.add_field(name="!pause", value="Pauses the song", inline=True)
      embed.add_field(name="!toggledj", value="Toggles if only dj's can play songs", inline=True)
      await message.channel.send(embed=embed)
      # Lists all music commands.

    if message.content.startswith('/eco'):
      embed=discord.Embed(title=" ", description=" ")
      embed.set_author(name="!music")
      embed.add_field(name="No Commands avalible yet.", value="Try again soon.", inline=True)
      await message.channel.send(embed=embed)
      # Lists all economy commands.
    
    if message.content.startswith('/general'):
      embed=discord.Embed(title=" ", description=" ")
      embed.set_author(name="!music")
      embed.add_field(name="No Commands avalible yet.", value="Try again soon.", inline=True)
      await message.channel.send(embed=embed)
      # Lists all general commands.
    
    if message.content.startswith('/adminc'):
      embed=discord.Embed(title=" ")
      embed.set_author(name="Administrator Commands")
      embed.add_field(name="!clear", value="Clears a number of messages", inline=True)
      embed.add_field(name="!purge", value="Clears a whole channel", inline=True)
      embed.add_field(name="!ban", value="Bans a user from the server", inline=True)
      embed.add_field(name="!tempban [s, m, h, d]", value="Bans a user from the server for a certian period", inline=True)
      embed.add_field(name="!kick", value="Kicks a user from the server", inline=True)
      embed.add_field(name="!mute", value="Mutes a user from the server", inline=True)
      embed.add_field(name="!mute [s, m, h, d]", value="Mutes a user from the server for a certian period", inline=True)
      embed.add_field(name="!admin", value="Gives a user administrator role", inline=True)
      embed.add_field(name="!mod", value="Gives a user moderator role", inline=True)
      await message.channel.send(embed=embed)
      # Lists all administrator commands.





    if message.content.startswith('/joindate'):
      dt = datetime.fromtimestamp(message.author.created_at.timestamp())
      dt = str(dt)
      obj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')
      await message.channel.send('Hacking discord.com/urmom69420/joindate...')
      time.sleep(1.5)
      await message.channel.send('Accessing libraries...')
      time.sleep(0.5)
      await message.channel.send('Getting packages...')
      time.sleep(0.5)
      await message.channel.send('Opening discorduserinfo.txt...')
      time.sleep(0.5)
      await message.channel.send('Deleting discord account...')
      time.sleep(2)
      await message.channel.send('Making another discord account...')
      time.sleep(2)
      await message.channel.send('Accessing discord database...')
      time.sleep(2)
      await message.channel.send('Grabbing user token...')
      time.sleep(2)
      await message.channel.send('Stealing account...')
      time.sleep(3)
      if str(obj.month) == '1':
        await message.channel.send('Your account was created on ' + 'January' + ' ' + str(obj.day) + ' ' + str(obj.year) + '❄️!')
      
      if str(obj.month) == '2':
        await message.channel.send('Your account was created on ' + 'Febuary' + ' ' + str(obj.day) + ' ' + str(obj.year) + '❤️!')

      if str(obj.month) == '3':
        await message.channel.send('Your account was created on ' + 'March' + ' ' + str(obj.day) + ' ' + str(obj.year) + '☘️!')

      if str(obj.month) == '4':
        await message.channel.send('Your account was created on ' + 'April' + ' ' + str(obj.day) + ' ' + str(obj.year) + '🐰!')

      if str(obj.month) == '5':
        await message.channel.send('Your account was created on ' + 'May' + ' ' + str(obj.day) + ' ' + str(obj.year) + '🪅!')

      if str(obj.month) == '6':
        await message.channel.send('Your account was created on ' + 'June' + ' ' + str(obj.day) + ' ' + str(obj.year) + '☀️!️')
      
      if str(obj.month) == '7':
        await message.channel.send('Your account was created on ' + 'July' + ' ' + str(obj.day) + ' ' + str(obj.year) + '🧨!')

      if str(obj.month) == '8':
        await message.channel.send('Your account was created on ' + 'August' + ' ' + str(obj.day) + ' ' + str(obj.year) + '📚!')
      
      if str(obj.month) == '9':
        await message.channel.send('Your account was created on ' + 'September' + ' ' + str(obj.day) + ' ' + str(obj.year) + '🍂!')
      
      if str(obj.month) == '10':
        await message.channel.send('Your account was created on ' + 'Ocotober' + ' ' + str(obj.day) + ' ' + str(obj.year) + '🎃!')

      if str(obj.month) == '11':
        await message.channel.send('Your account was created on ' + 'November' + ' ' + str(obj.day) + ' ' + str(obj.year) + '🦃!')

      if str(obj.month) == '12':
        await message.channel.send('Your account was created on ' + 'December' + ' ' + str(obj.day) + ' ' + str(obj.year) + '🎄!')


    if message.content.startswith('/work'):
        await message.channel.send('Not Avalible yet.')
        # Go to your job.

    if message.content.startswith('/bal'):
        await message.channel.send('Not Avalible yet.')
        # Account balance.

    if message.content.startswith('/balance'):
        await message.channel.send('Not Avalible yet.')
        # Account balance.

    if message.content.startswith('/job'):
        await message.channel.send('Not Avalible yet.')
        # Shows your job.

    if message.content.startswith('/search'):
      x = random.randint(1, 100)
      rand = random.randrange(len(searchloc))
      random_str = searchloc[rand]
      await message.channel.send('You found $' + str(x) + ' in your ' + str(random_str))
      # Looks for money.

    if message.content.startswith('/clear'):
        await message.channel.send('Not Avalible yet.')
        # Clears number of messages.

    if message.content.startswith('/purge'):
        await message.channel.send('Not Avalible yet.')
        # Deletes channel and makes it again.

    if message.content.startswith("/spam"):
      for x in range(0,10, 1):
        await message.channel.send("looooooooooool")
        time.sleep(1)
      await message.channel.send("Ok i'm done.")
      # Spams 10 messages.

    if message.content.startswith('idkjustdonttypethiswowyoutypedthisoknowstopchickennugget'):
      await message.channel.send('how, just how.')













@client.event
async def on_member_join(member):
    print(str(member) + " joined")
    with open("database.json"  ,"a"  ) as file:
      pass
    
    # send message to join logs
    channel = discord.utils.get(member.guild.text_channels,name = "join-log")
    await channel.send( f"{member} has joined.")

    await member.send("Welcome!")
    












@client.event
async def on_member_remove(member):
    print(str(member) + " left")





client.run('ODMwODM5NTIwNjMwNTM4MzAx.YHMhmQ.bCaM_spkfg6h4DXK6kJRktFuKvQ')
# Logs in with discord token




'''
1. User joins server
user = {
  "wallet" : 0,
  "join_date" : None,
  "howmany_text" : None,
  "howlong_voice" : None,
  ""
}

Gains? 
1. Talk but not spam
2. emploment system
3. how long you joined voice for
4. how long you joined the server



{
  "usename" : 
  {
    "id" : "461693891047233730",
    "messages" : [69,420],
    "money" : 0.0,
    "lastsearch" : datetime object,
    "timeinserver" : 0
  }
}




dictonaries are curly brackets 
each item inside a dictionary is KEY:VALUE,

'''
