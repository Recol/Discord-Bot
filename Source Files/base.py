
from time import sleep
import discord
import uiautomation as automation
from discord import client
from discord.ext import commands
from discord.ext.commands import Context
from uiautomation import Control

BOT_PREFIX = ("!", ".")
TOKEN = "insert your own"
bot = commands.Bot(command_prefix=BOT_PREFIX)


@bot.command(name='change',
             description="Change the status of the bot",
             aliases=['update_status', 'clear_chat'],
             pass_Context=True)
async def update_status(ctx):
    if __name__ == '__main__':
        # sleep function designed to hook the omnibox URL
        sleep(3)
        control: Control = automation.GetFocusedControl()
        controlList = []
        while control:
            controlList.insert(0, control)
            control = control.GetParentControl()
        if len(controlList) == 1:
            control = controlList[0]
        else:
            control = controlList[1]
        address_control = {automation.FindControl(control, lambda c, d: not (not isinstance(c,
                                                                                            automation.EditControl)))}
    URL = address_control.CurrentValue()
    # split the URL into a readable format
    sep = '/'
    split_URL = URL.split(sep, 1)[0]
    await ctx.send(split_URL)


@bot.command(pass_Context=True)
async def clear(ctx, amount=200):
   #basic clearing function
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
        await client.delete_messages(messages)
        await client.say('Cleared chat.')


bot.run(TOKEN)
