import asyncio
import discord

intents = discord.Intents.all()

client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send(f"Pongado {message.author.mention}.")

    if message.content.startswith('$pergunta'): ##Qualquer pessoa pode responder a pergunta, não só a primeira pessoa que executou $pergunta
        channel = message.channel
        await channel.send('Responda qualquer coisa!')

        def check(m):
            return m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send(f'Ola {msg.author}, você respondeu {msg.content}!')
        
    if message.content.startswith('$thumb'):
        channel = message.channel
        old_message = await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

client.run('MTAxNDYzODEzNDI3OTAzMjg3Mg.GJR2zO.ZQqGSebZWqxlK6NU_D1kCdaUvEY6GRHEBsY9kw')
