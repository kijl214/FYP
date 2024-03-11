import discord

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Get the channel object for the test channel
    test_channel = client.get_channel(1109072121474334762) # Replace with the actual channel ID

    # Open the image file and create a discord.File object
    with open('savedimage.jpg', 'rb') as f:
        image = discord.File(f)

    # Send the image to the test channel
    try:
        await test_channel.send(file=image)
        print('Image sent to test channel successfully')
    except:
        print(f'Failed to send image to test channel {test_channel.name}')

    # Close the client connection
    async with client:
        print('Client connection closed successfully')

# Start the Discord bot and run the event loop
client.run('MTEwOTA2MzY1NTg4ODI3NzU0NQ.G5oy5F.7nepOqfU9B6lnPXa-L3KEXhLQrSErV-0f8QDbs')

# Continue running the script after the bot has stopped
print('Bot has stopped')