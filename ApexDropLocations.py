#bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    Worlds_Edge = ['Bridge', 'Dome', 'Epicenter', 'Trials', 'Countdown', 'Fragment East', 'Fragment West', 'Geyser', 'Harvest', 'Hill Valley', 'Launch Site', 'Lava City', 'Lava Fissure', 'Mining Pass', 'Overlook', 'Rain Tunnel', 'Refinery', 'Staging', 'Skyhook', 'Sorting Factory', 'Springs End', 'Survey Camp', 'Thermal Station', 'Tree', 'Train Yard']
    Olympus = ['Agriculture Entry', 'Antechamber', 'Autumn Estates', 'Bonzai Plaza', 'Arcadia Supercarrier', 'Cargo hold', 'Central Turbine', 'Crossroads', 'Defense Perimmter', 'Docks', 'Elysium', 'Energy Depot','Farmstead', 'Grow Towers', 'Golden Gardens', 'Hammond Labs', 'Hydroponics', 'Ivory Pass', 'Maintenance', 'Orbital Cannon Test Site', 'Phase Gateway Central', 'Primary Power Grid', 'Rift Aftermath', 'Research Basin', 'Secondary Power Grid', 'Shipyard', 'Solar Array', 'Supply Track', 'The Reverie Lounge', 'Underpass', 'Velvet Oasis', 'Welcome Center', 'Wildflower Meadow']
    Kings_Canyon = ['Airbase', 'ARES Capacitor', 'Artillery Battery', 'Artillery Tunnel', 'Artillery Underpass', 'Broken Coast', 'Broken Coast Overlook', 'Broekn Coast South', 'Bunker Pass', 'Cage', 'Capacitor Junction', 'Capacitor Overlook', 'Capacitor Tunnel', 'Caves', 'Creature Containment', 'Crossroads', 'Cryptos Map Room', 'Destroyed Bridges', 'Destroyed Cascades', 'East Settlement', 'The Farm', 'Golden Sands', 'High Desert', 'Hillside Outpost', 'Hydro Dam', 'Hydro Tunnel', 'Interstellar Relay', 'Marketplace', 'Octanes Gauntlet', 'Offshore Rig', 'Offshore Rig Loading', 'Reclaimed Forest', 'Repulsore', 'Rivers End','River Center', 'Runoff', 'Skull Salvage', 'Singh Labs', 'Singh Labs Interior', 'Suspended Skull', 'Slum Lakes', 'Swamps', 'Terminal Station F-85', 'Terminal Station L-19', 'Terminal Station O-240', 'Terminal Station W-73', 'The Pit', 'Two Spines', 'Two Spines Outpost', 'Watchtower North', 'Watchtower South', 'Water Treatment', 'Waterfall']

    if message.content == '!drop Worlds Edge':
        response = random.choice(Worlds_Edge)
        await message.channel.send(response)

    if message.content == '!drop Olympus':
        response = random.choice(Olympus)
        await message.channel.send(response)
    
    if message.content == '!drop Kings Canyon':
        response = random.choice(Kings_Canyon)
        await message.channel.send(response)

client.run(TOKEN)
