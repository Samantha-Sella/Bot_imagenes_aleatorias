import discord
from discord.ext import commands
import os
import random
import requests

intents= discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como{bot.user}")

@bot.command()
async def meme(ctx):
    imagenes = os.listdir("imagenes")
    imagen_aleatoria = random.choice(imagenes)
    with open(f"imagenes/{imagen_aleatoria}", "rb") as f:
        imagen = discord.File(f)
    await ctx.send(file=imagen)

def obtener_pato():
    url = "https://random-d.uk/api/random"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos ["url"]

@bot.command()
async def pato(ctx):
    url_imagen =obtener_pato()
    await ctx.send(url_imagen)

bot.run("aca va el token de tu bot.")
