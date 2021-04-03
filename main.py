import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad","depressed","unhappy","angry","miserable","depressing","failed","failure","fail","loose","lost"]

starter_encouragements = [
  "cheer up !",
  "hang in there !",
  "every day is a blessing",
  "welcome today you are gonna be happy",
  "you are a great person",
  "you are capable more than you think you are"
]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "  _" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encuragements" is db.key():
    encouragements = db["encouragements"]
    encouragements.append(encouraging )

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client:
      return
    
    msg = message.content

    if message.content.startswith('$hello'):
      await message.channel.send('hello !')
      

    if message.content.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))