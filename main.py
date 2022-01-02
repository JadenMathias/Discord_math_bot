import discord
import sys
sys.path.insert(0, 'D:\Desktop\Projects\Discord_math_bot\Expression Objects')
from expression import Variable
from processor import Processor
from discord.ext import commands

client = commands.Bot(command_prefix = '>')

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
    await ctx.send("Use :  derivate 'enter expression here' 'variable here'  \n ( Make sure to encapsulate the expression in double quotes)")

@client.command()
async def derivate(ctx, expression, wrt): 
    x = dydx(expression,wrt)
    await ctx.send(x)

    
client.run('OTI1NDQwNjczNDIxODY5MTE2.YctJyg.S8Q_wRjoDrsXgmu_TjG-Cxgg1Pw')