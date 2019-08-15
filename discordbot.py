from discord.ext import commands
import os
import traceback

bot = commands.Bot(command＿prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        await bot.process_commands(message)
     except Exception:
        await message.channel.send(f'```\n{traceback.format_exc()}\n```')
        @bot.commands
        async def ping(ctx):
            await ctx.send('pong')
            
            @bot.commands
            async def kuso(ctx):
                await ctx.send('wakaru')
                
                bot.run(token)
            
                   
                   
