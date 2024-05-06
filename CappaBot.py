import asyncio
import discord
from discord import app_commands
import os
import sys
import random
from dotenv import load_dotenv
# Casper changes here
# CappaBot.py
print("CappaBot has started loading...")

# Enivornment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CAPPABOT = int(os.getenv("DISCORD_CAPPABOT_ID"))

# Constant variables
DEBUG = False
REACTION_IMAGE_PATH = "../reactionImages/"
REACTION_IMAGE_NAMES = os.listdir(REACTION_IMAGE_PATH)
SERVER = discord.Object(948070330486882355)

# Basic variables
personToReact = 0
personToCopy = 0

print(f"Last 4 digits of bot token: {TOKEN[-4:]}")
print(f"CappaBot ID: {CAPPABOT}")
print(f"Server: {SERVER}")

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@tree.command(
	description="I will reply with 'pong' as fast as I can."
)
async def ping(interaction):
	print("Got ping command")
	print(interaction)
	await interaction.response.send_message("Pong")

@tree.command(
	description="Stop me."
)
async def stop(interaction):
	print("Stopping from the stop command.")
	await interaction.response.send_message("Ok, I'll stop now.")
	sys.exit("Someone told me to stop.")

@tree.command(
	description="I will react to the user you specify."
)
async def react(interaction):
	global personToReact
	print("I should react to")
	personToReact = 797563949204897893
	await interaction.response.send_message("I will react to [cappa]")

@tree.command(
	description="I will copy the user you specify."
)
async def copy(interaction):
	global personToCopy
	print("I should copy")
	personToCopy = 797563949204897893
	await interaction.response.send_message("I will copy [cappa]")

class VoiceGroup(app_commands.Group):
	@app_commands.command(
		name="connect",
		description="Connect to a voice channel"
	)
	async def connect(self, interaction):
		print("Connect command")
		await interaction.response.send_message("I will connect to")

	@app_commands.command(
		name="disconnect",
		description="Disconnect from the current voice call I am in."
	)
	async def disconnect(self, interaction):
		print("Disconnect command")
		await interaction.response.send_message("Disconnecting...")

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

	voiceGroup = VoiceGroup(name="voice", description="The voice commands can make me connect and disconnect from a voice call.")
	tree.add_command(voiceGroup)

	tree.copy_global_to(guild=SERVER)
	await tree.sync(guild=SERVER)

	if DEBUG:
		user = client.get_user(CAPPABOT)
		await user.send("Cappa Bot has started")

		#channel = client.get_channel(CHANNEL)
		#await channel.send("Cappa Bot is online")

# When someone send a message
@client.event
async def on_message(message):
	global personToReact
	global personToCopy
	# Print the message info
	print(message)

	# If the message was sent in a DM to the bot
	if message.guild:
		# If the message was sent by a bot
		if message.author.bot:
			print("Messsage sent by bot")

			# If the message was sent by me
			if message.author.name == "Cappa Bot":
				print(f"Message was sent by me in: {message.guild.name} > {message.channel.name} | {message.content}")
			# If the message was sent by dad bot
			if message.author.name == "Dad Bot":
				# Say shut up dad bot
				await message.reply("Shut up dad bot.")
			
		# If the message was not sent by a bot	
		else:
			# Print message details
			print(f"""Message in text channel. Details:
	Server: {message.guild.name}
	Channel: {message.channel.name}
	Sent from: {message.author}
	Contents: {message.content}""")
			
			# Check if from Niv
			#if message.author.name == "drporknswine":
			#	await message.channel.send("<@783924515549347870> said something")

			# Check if I need to react to the person
			if message.author.id == personToReact:
				# React to them
				print("I should react to that")
				reactionImage = REACTION_IMAGE_PATH + random.choice(REACTION_IMAGE_NAMES)
				await message.reply("", file=discord.File(reactionImage))
			
			# Check if I need to copy the person
			if message.author.id == personToCopy:
				# Copy them
				print("I should copy that")
				await message.channel.send(message.content)

	# If the message was sent in a text channel
	else:
		print(f"""Message in DM's. Details:
	Sent from: {message.author.name} / {message.author.global_name}
	Contents: {message.content}""")
	
	print("-"*50)

client.run(TOKEN)

#CHANNEL.send("Cappa Bot died :(")

print("Cappa Bot has ended.") 