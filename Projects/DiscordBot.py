import discord
import requests
import json
import random
import os

# --- File to save XP data ---
XP_FILE = "user_xp.json"

# --- Load XP from file ---
def load_xp():
    if os.path.exists(XP_FILE):
        with open(XP_FILE, "r") as f:
            return json.load(f)
    return {}

# --- Save XP to file ---
def save_xp():
    with open(XP_FILE, "w") as f:
        json.dump(user_xp, f, indent=4)

# --- Fun APIs ---
def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response.text)
    return json_data["url"]

def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
    json_data = json.loads(response.text)
    if json_data["type"] == "single":
        return json_data["joke"]
    else:
        return json_data["setup"] + " - " + json_data["delivery"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    return f"“{json_data[0]['q']}” – {json_data[0]['a']}"

# --- XP System ---
user_xp = load_xp()   # Load from file

def add_xp(user_id):
    user_id = str(user_id)  # Convert to string for JSON keys
    if user_id not in user_xp:
        user_xp[user_id] = {"xp": 0, "level": 1}
    
    user_xp[user_id]["xp"] += 10  # +10 XP per message
    xp = user_xp[user_id]["xp"]
    level = user_xp[user_id]["level"]
    next_level = level * 50  # XP needed for next level

    if xp >= next_level:
        user_xp[user_id]["level"] += 1
        user_xp[user_id]["xp"] = 0
        save_xp()
        return f"🎉 Congrats <@{user_id}>! You leveled up to **Level {user_xp[user_id]['level']}**!"
    
    save_xp()
    return None

# --- Bot Client ---
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # XP System
        level_up_msg = add_xp(message.author.id)
        if level_up_msg:
            await message.channel.send(level_up_msg)

        # Commands
        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())

        elif message.content.startswith("$joke"):
            await message.channel.send(get_joke())

        elif message.content.startswith("$quote"):
            await message.channel.send(get_quote())

        elif message.content.startswith("$8ball"):
            responses = [
                "Yes", "No", "Maybe", "Definitely", "Ask again later", 
                "It is certain", "Outlook not so good", "You will find out soon"
            ]
            await message.channel.send(random.choice(responses))

        elif message.content.startswith("$level"):
            uid = str(message.author.id)
            if uid in user_xp:
                await message.channel.send(f"🧙 {message.author.mention}, you are Level {user_xp[uid]['level']} with {user_xp[uid]['xp']} XP!")
            else:
                await message.channel.send(f"🧙 {message.author.mention}, you haven’t earned any XP yet.")

# --- Run Bot ---
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('Discord Key")
