# Import Discord Package
import discord

# Client (our bot)
client = discord.Client()

@client.event
async def on_ready():
    # DO STUFF....
    general_channel = client.get_channel(772169387104141336)

    await general_channel.send('Hello, world')

# Run the client on the server
client.run('NzczMjM4NjQ1OTY3ODE0NjU3.X6GUmw.-Kym0qjEs96c1qmZ1GPZWGOtZ1Y')