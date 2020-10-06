import discord
from discord.ext import commands

client=discord.Client()
arquivo=open('listausuarios.txt','x')
arquivo2=open('listanicks.txt','x')

@client.event
async def on_ready():
	print('Loggd in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	print('bot is ready')
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return
		
	if message.content.startswith("!op"):
		message.content = message.content[4:]
		arquivo.write(message.content)
		arquivo.write('\n')
		arquivo2.write(message.author.name)
		arquivo2.write('\n')
		message.content = message.content.replace(' ','+')
		response=f'https://br.op.gg/summoner/userName={message.content}'
		await message.channel.send(response)
		
		
client.run('coloque o codigo do site aqui')
arquivo.close()
arquivo2.close()
