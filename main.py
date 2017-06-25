import discord
from discord.ext.commands import Bot
from discord import User
from discord import Client
import random
import sys


def get_token():
    token = []
    with open("token.cfg") as f:
        token = f.read().splitlines()
    token = list(filter(None, token))
    return token[0]


def add_text(text, fname):
    with open(fname, 'a') as file:
        file.writelines("\n" + text)


def quote_exists(text, fname):
    quotes = []
    with open(fname) as f:
        quotes = f.read().splitlines()
    if text in quotes:
        return True
    return False


def get_from_list(fname):
    quotes = []
    with open(fname) as f:
        quotes = f.read().splitlines()
    quotes = list(filter(None, quotes))
    return random.choice(quotes)

my_bot = Bot(command_prefix=".")


@my_bot.event
async def on_read():
    print("Client logged in")


@my_bot.command()
async def hello():
    return await my_bot.say(get_from_list("hello.txt"))


@my_bot.command()
async def ha():
    return await my_bot.say("GAYYYYYYYYYYYYYYYYYYYYYYYYYY!")


@my_bot.command()
async def test(*args):
    return await my_bot.say("Hello " + str(args))


@my_bot.command()
async def quote():
    return await my_bot.say(get_from_list("quotes.txt"))


@my_bot.command()
async def trivia():
    return await my_bot.say(get_from_list("trivia.txt"))


@my_bot.command()
async def all_quotes():
    quotes = []
    with open("quotes.txt") as f:
        quotes = f.read().splitlines()
    quotes = list(filter(None, quotes))
    print(quotes)
    for quote in quotes:
        await my_bot.say(quote)


@my_bot.command()
async def all_trivia():
    quotes = []
    with open("trivia.txt") as f:
        quotes = f.read().splitlines()
    quotes = list(filter(None, quotes))
    print(quotes)
    for quote in quotes:
        await my_bot.say(quote)


@my_bot.command()
async def sleep():
    return await my_bot.say("Sleep is for the weak!")


@my_bot.command()
async def kill():
    await my_bot.say(get_from_list("mercy.txt"))
    sys.exit()


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

@my_bot.command()
async def man():
    quotes = []
    with open("help.txt") as f:
        quotes = f.read().splitlines()
    for quote in quotes:
        await my_bot.say(quote)


my_bot.run(get_token())