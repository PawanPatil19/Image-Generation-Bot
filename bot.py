import discord
from discord.ext import commands
import datetime
import asyncio
import random
from instabot import Bot

from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


bot = Bot()
bot.login(username="cphub.nitc", password="hellopc12")


client = commands.Bot(command_prefix = ">")
client.remove_command("help")

@client.event
async def on_ready():
	print("Bot is ready")

@client.group(invoke_without_command=True)
async def help(ctx):
	em = discord.Embed(title = "Help", description = "Use >help for information of the commands required to generate a contest image")

	em.add_field(name = "name", value="Contest Name")
	em.add_field(name = "time", value="Contest Time")
	em.add_field(name = "date", value="Contest Date")
	em.add_field(name = "upload_mirror", value="Upload to Instagram")
	em.add_field(name = "upload_beginner", value="Upload to Instagram")

	await ctx.send(embed = em)


@client.command()
async def name(ctx, *, text = "No test entered"):

	img = Image.open("template.jpg")

	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("Amatic-Bold.ttf", 125)
	draw.text((210,255), text, (0,0,0), font = font)

	img.save("c.jpg")
	name1 = text
	embed=discord.Embed(title="Contest Name Added", description=text, color=0x00ff00)
	
	await ctx.send(embed = embed)
	

@client.command()
async def date(ctx, *, text = "No test entered"):

	img = Image.open("c.jpg")

	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("OpenSans.ttf", 50)
	draw.text((620,550), text, (0,0,0), font = font)

	img.save("c1.jpg")
	date1 = text
	embed=discord.Embed(title="Date Added", description=text, color=0x00ff00)
	
	await ctx.send(embed = embed)

@client.command()
async def time(ctx, *, text = "No test entered"):

	img = Image.open("c1.jpg")

	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("OpenSans.ttf", 50)
	draw.text((620,660), text, (0,0,0), font = font)

	img.save("c2.jpg")
	time1 = text
	embed=discord.Embed(title="Time Added", description=text, color=0x00ff00)
	
	await ctx.send(embed = embed)
	await ctx.send(file = discord.File("c2.jpg"))



@client.command()
async def upload_beginner(ctx, *, text):	
	
	upload_text = '''
	Greetings,

    We are glad to invite you to take part in CP Hub Beginner Contest. This contest will be held on Virtual Judge. You will be given 6-8 problems and 2 hours to solve them. You guys can participate in a team of 3 members wherein you can discuss the strategy, logic, code, etc and submit your solutions.
    Contest link: {}
	Start time: 10:00 AM (IST)
    Contest Duration: 2:00 hours

    Editorials will be sent to your mail after the contest.
    All The Best.

	-CP Hub, Nitc'''.format(text)
	embed=discord.Embed(title="Uploaded", description=upload_text, color=0x00ff00)
	
	await ctx.send(embed = embed)
	bot.upload_photo("c2.jpg", caption= upload_text)
	
@client.command()
async def upload_mirror(ctx,*, text):	
	upload_text = '''
	Greetings,

    We are glad to invite you to take part in NITC ICPC Mirror. This contest will be held on Virtual Judge. You will be given 8-12 previous ICPC Regionals problems and 5 hours to solve them. You guys can participate in a team of 3 members wherein you can discuss the strategy, logic, code, etc and submit your solutions.

    Contest link: {}
	Start time: 10:00 AM (IST)
    Contest Duration: 5:00 hours

    Editorials will be sent to your mail after the contest.
    All The Best.

	-CP Hub, Nitc'''.format(text)
	embed=discord.Embed(title="Uploaded", description=upload_text, color=0x00ff00)
	
	await ctx.send(embed = embed)
	bot.upload_photo("c2.jpg", caption= upload_text)	




client.run("ODIzODM5MjYzODk1MzIyNjM0.YFmqGg.zJO6EgvRHGnHGRAWYYTKvW6Gs6M")



