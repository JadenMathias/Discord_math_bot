import sys
sys.path.insert(0, 'D:\Desktop\Projects\Discord_math_bot\Expression Objects')
import discord
import os
from expression import Variable
from processor import Processor
from discord.ext import commands
from dotenv import load_dotenv

BOT_TOKEN = os.environ.get('BOT_TOKEN')

client = commands.Bot(command_prefix = '>' , help_command=None)

def dydx(exp , wrt):
    parser = Processor()
    x = parser.parse(exp)
    y = parser.parse(wrt)
    #print("Expression:", x)
    x = x.derivate(y)
    while x != x.simplify():
        x = x.simplify()
    return "Derivative: " + str(x)


@client.event          
async def on_ready():
    print("Bot ready")

@client.command()
async def help(ctx):
   await ctx.send("""
Commands:\n
derivate \"Expression\" 'Variable'\n
Usage:\n
Expression example : "-sin(x) + 2 * log(3^x - 1/x)"
   """)


@client.command()
async def derivate(ctx, expression, wrt = None):
    try:
        if wrt == None:
            await ctx.send("Try again! No variable to derivate with was found! Use help if lost :)")
            return
        x = dydx(expression,wrt)
        await ctx.send(x)
    except:
        await ctx.send("Incorrect usage of command/expression. Use help if lost :)")

    
client.run(BOT_TOKEN)
