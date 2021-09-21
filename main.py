import discord
import requests
import os

client = discord.Client()

@client.event
async def on_ready():
  print("Bot ready!")

@client.event
async def on_message(message):
  # If message from bot itself
  if(message.author == client.user):
    return

  text = message.content.lower()

  if(message.content.startswith('>')):
    if(text[1:] == "hello"):
      await message.channel.send('Hello {0}'.format(message.author.mention))

    if("happy" in text):
      await message.channel.send(":smile:")


    if("sad" in text):
      await message.channel.send(":cry:")

    if(text.startswith(">add")):
      text = text.replace(">add ", "")
      a, b = map(int, text.split(", "))
      ans = a+b
      await message.channel.send("Ans: {0}".format(ans))

    if(text.startswith(">subt")):
      text = text.replace(">subt ", "")
      a, b = map(int, text.split(", "))
      ans = a - b
      await message.channel.send("Ans: {0}".format(ans))

    if(text.startswith(">mult")):
      text = text.replace(">mult ", "")
      a, b = map(int, text.split(", "))
      ans = a * b
      await message.channel.send("Ans: {0}".format(ans))

    if(text.startswith(">div")):
      text = text.replace(">div ", "")
      a, b = map(int, text.split(", "))
      ans = a / b
      await message.channel.send("Ans: {0}".format(ans))

    if(text.startswith(">fdiv")):
      text = text.replace(">fdiv ", "")
      a, b = map(int, text.split(", "))
      ans = a // b
      await message.channel.send("Ans: {0}".format(ans))

client.run(os.getenv("Token"))
