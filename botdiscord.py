import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MeuCliente(discord.Client):
    async def on_ready(self):
        print(f"Logado como {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.lower().strip().startswith('!testando'):
            await message.channel.send('tudo certo!')
        if message.content.lower().strip().startswith('!meme'):
            await message.channel.send(get_meme())


intents = discord.Intents.default()
intents.message_content = True

client = MeuCliente(intents=intents)
client.run("SEU TOKEN AQUI") # Substitua pelo seu token