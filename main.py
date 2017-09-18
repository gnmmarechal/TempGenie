import discord
from discord.ext.commands import Bot
from discord import User
from discord import Client
import random
import sys


# Gets the token from a config file
def get_token():
    token = []
    with open("token.cfg") as f:
        token = f.read().splitlines()
    token = list(filter(None, token))
    return token[0]


# Writes text to a file as a new line
def add_text(text, fname):
    with open(fname, 'a') as file:
        file.writelines("\n" + text)


# Checks if a line exists in a file
def quote_exists(text, fname):
    quotes = []
    with open(fname) as f:
        quotes = f.read().splitlines()
    if text in quotes:
        return True
    return False


# Returns a random non-empty line from a file
def get_from_list(fname):
    quotes = []
    with open(fname) as f:
        quotes = f.read().splitlines()
    quotes = list(filter(None, quotes))
    return random.choice(quotes)

# Initializes the bot and sets the command prefix
my_bot = Bot(command_prefix=".")


@my_bot.event
async def on_read():
    print("Client logged in")


# Makes the bot say hello
@my_bot.command()
async def hello():
    return await my_bot.say(get_from_list("hello.txt"))


# Makes the bot reply "GAY"
@my_bot.command()
async def ha():
    reply = "GA"
    i = random.randint(0, 90)
    while i > 0:
        reply += "Y"
        i -= 1
    reply += "!"
    return await my_bot.say(reply)


@my_bot.command()
async def cerise():
    return await my_bot.say("weeb")


@my_bot.command()
async def f(alias="F"):
    return await my_bot.say("Paying respects...")


# Makes the bot reply "Hello" followed by a the arguments
@my_bot.command()
async def test(*args):
    return await my_bot.say("Hello " + str(args))


# Makes the bot say a random quote
@my_bot.command()
async def quote(number = 1):
	if number < 1:
		number = 1
	for number in range(0, number):
		await my_bot.say(get_from_list("quotes.txt"))
	
	return
    
    
# Makes the bot say a random quote
async def tts_quote():
    return await my_bot.say("/tts " + str(get_from_list("quotes.txt")))



# Makes the bot wofl wofl
@my_bot.command()
async def wofl():
	pofl_gen = random.randint(0, 100)
	is_pofl = False
	if pofl_gen < 5:
		is_pofl = True
	
	reply = "wofl"
	if is_pofl:
		reply = "pofl"
	i = random.randint(0, 35)
	while i > 0:
		if is_pofl:
			reply += " pofl"
		else:
			reply += " wofl"
		i -= 1
	reply += "!"
	return await my_bot.say(reply)

# No pofl for you
@my_bot.command()
async def pofl():
	return await my_bot.say("No pofl for you!")

# Senpai no baka!
@my_bot.command()
async def baka():
	paka_gen = random.randint(0, 100)
	is_paka = False
	if paka_gen < 5:
		is_paka = True
	
	number_of_bakas = random.randint(1, 31)
	str1 = "b"
	if is_paka:
		str1 = "p"
	for baka in range(number_of_bakas - 1):
		a1 = random.randint(1,11)
		for a in range(a1):
			str1 += "a"
		str1 += "k"
		a2 = random.randint(1,11)
		for a in range(a2):
			str1 += "a"
		if is_paka:
			str1 += " p"
		else:
			str1 += " b"
	a1 = random.randint(1,11)
	a2 = random.randint(1,11)
	for a in range(a1):
		str1 += "a"
	str1 += "k"
	for a in range(a2):
		str1 += "a"
	str1 += "!"
	return await my_bot.say(str1)
	
	
# Makes the bot shrug
@my_bot.command()
async def shrug():
	return await my_bot.say("https://media.discordapp.net/attachments/329063968570081281/353170075479441409/Untitled-6.gif")
	

# Makes the bot shrug
@my_bot.command()
async def halp():
	return await my_bot.say("https://www.youtube.com/watch?v=pgnO_Mbmns4")
	

# Makes the bot say random trivia
@my_bot.command()
async def trivia(alias="t"):
    return await my_bot.say(get_from_list("trivia.txt"))


# Makes the bot reply with all available quotes
@my_bot.command()
async def all_quotes(alias="aq"):
    quotes = []
    with open("quotes.txt") as f:
        quotes = f.read().splitlines()
    quotes = list(filter(None, quotes))
    print(quotes)
    for quote in quotes:
        await my_bot.say(quote)


# Makes the bot reply with all available trivia
@my_bot.command()
async def all_trivia():
    quotes = []
    with open("trivia.txt") as f:
        quotes = f.read().splitlines()
    quotes = list(filter(None, quotes))
    print(quotes)
    for quote in quotes:
        await my_bot.say(quote)


# Makes the bot reply with its opinion on sleep
@my_bot.command()
async def sleep():
    return await my_bot.say("Sleep is for the weak!")


# Kills the bot
@my_bot.command()
async def kill(alias="die"):
    await my_bot.say(get_from_list("mercy.txt"))
    sys.exit()


# Adds a quote to the list
@my_bot.command()
async def add_quote(*args):
    final_quote = ""
    for arg in args:
        final_quote += str(arg) + " "
    final_quote = final_quote[:-1]
    print("Adding quote: " + final_quote)
    if not quote_exists(final_quote, "quotes.txt") and "TempGenie" not in final_quote:
        await my_bot.say("Adding quote: \"" + final_quote + "\"")
        add_text(final_quote, "quotes.txt")
    elif "TempGenie" in final_quote:
        await my_bot.say("You're not going to say things about me. 'kay?")
    else:
        await my_bot.say("Quote already exists!")


# Adds trivia to the list
@my_bot.command()
async def add_trivia(*args):
    final_quote = ""
    for arg in args:
        final_quote += str(arg) + " "
    final_quote = final_quote[:-1]
    print("Adding trivia: " + final_quote)
    if not quote_exists(final_quote, "trivia.txt") and "TempGenie" not in final_quote:
        await my_bot.say("Adding trivia: \"" + final_quote + "\"")
        add_text(final_quote, "trivia.txt")
    elif "TempGenie" in final_quote:
        await my_bot.say("You're not going to say things about me. 'kay?")
    else:
        await my_bot.say("Quote already exists!")


# Shows the help page
@my_bot.command()
async def man():
    quotes = []
    with open("help.txt") as f:
        quotes = f.read().splitlines()
    for quote in quotes:
        await my_bot.say(quote)

# Retard-related shit
@my_bot.command()
async def cv(*args):
	final_val = 0
	unit1 = float(args[0])
	unit1_1 = str(args[1])
	#unit2_1 = str(args[2])
	# Parse the type of unit
	u1 = []
	u2 = []
	si_units = [ "kg", "km", "ºC"]
	retard_units = [ "lb", "mile", "ºF"] 
	final_unit = "?"
	if unit1_1 in si_units:
		u1 = si_units
		u2 = retard_units
	else:
		u1 = retard_units
		u2 = si_units
	if unit1_1 == "lb" or unit1_1 == "pound":
		final_val = 0.45359237*unit1
		final_unit = "kg"
	if unit1_1 == "kg" or unit1_1 == "Kg":
		final_val = unit1 / 0.45359237
		final_unit = "lb"
	if unit1_1 == "km":
		final_val = unit1 / 1.609344
		final_unit = "miles"
	if unit1_1 == "mile":
		final_val = 1.609344 * unit1
		final_unit = "km"
	if unit1_1 == "C" or unit1_1 == "ºC":
		final_val = unit1 * (9/5) + 32
		final_unit = "ºF"
	if unit1_1 == "F" or unit1_1 == "ºF":
		final_val = (-32 + unit1) / (9/5)
		final_unit = "ºC"
		
	await my_bot.say(str(unit1) + " " + unit1_1 + " = " + str(final_val) + " " + final_unit)
		
	

# Runs the bot with the token
my_bot.run(get_token())
