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
    return await my_bot.say("GAYYYYYYYYYYYYYYYYYYYYYYYYYY!")


# Makes the bot reply "Hello" followed by a the arguments
@my_bot.command()
async def test(*args):
    return await my_bot.say("Hello " + str(args))


# Makes the bot say a random quote
@my_bot.command()
async def quote():
    return await my_bot.say(get_from_list("quotes.txt"))


# Makes the bot say random trivia
@my_bot.command()
async def trivia():
    return await my_bot.say(get_from_list("trivia.txt"))


# Makes the bot reply with all available quotes
@my_bot.command()
async def all_quotes():
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
async def kill():
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
    if not quote_exists(final_quote, "quotes.txt"):
        await my_bot.say("Adding quote: \"" + final_quote + "\"")
        add_text(final_quote, "quotes.txt")
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
    if not quote_exists(final_quote, "trivia.txt"):
        await my_bot.say("Adding trivia: \"" + final_quote + "\"")
        add_text(final_quote, "trivia.txt")
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


# Runs the bot with the token
my_bot.run(get_token())
