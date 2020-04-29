import discord
from discord.ext import commands

bot = commands.Bot("!")

emoji_oui = "👍"
emoji_non = "👎"
name_field_oui = "Oui "+emoji_oui
name_field_non = "Non "+emoji_non



@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

@bot.event
async def on_reaction_add(reaction,user):
    if reaction.message.author == bot.user and user != bot.user:
        if reaction.emoji == emoji_oui or reaction.emoji == emoji_non:
            current_embed = reaction.message.embeds[0]
            current_fields = current_embed.fields
            lines_oui = []
            index_oui = 0
            lines_non = []
            index_non = 0
            for field in current_fields:
                if field.name == name_field_oui:
                    lines_oui = field.value.split('\n')
                    index_oui = current_fields.index(field)
                if field.name == name_field_non:
                    lines_non = field.value.split('\n')
                    index_non = current_fields.index(field)
            is_emoji_oui = reaction.emoji ==  emoji_oui
            if is_emoji_oui:
                if user.name not in lines_oui:
                    lines_oui[0] = str(int(lines_oui[0])+1)
                    lines_oui.append(user.name)
                if user.name in lines_non:
                    lines_non[0] = str(int(lines_non[0])-1)
                    lines_non.remove(user.name)
            else:
                if user.name not in lines_non:
                    lines_non[0] = str(int(lines_non[0])+1)
                    lines_non.append(user.name)
                if user.name in lines_oui:
                    lines_oui[0] = str(int(lines_oui[0])-1)
                    lines_oui.remove(user.name)
            current_embed.set_field_at(index = index_oui, name = name_field_oui, value = '\n'.join(lines_oui))
            current_embed.set_field_at(index = index_non, name = name_field_non, value = '\n'.join(lines_non))
            await reaction.message.edit(embed = current_embed)
            await reaction.remove(user)   




@bot.command()
async def compris(ctx):
    embed = discord.Embed()
    embed.title = "As-tu compris?"
    embed.color = discord.Colour.blue()
    embed.add_field(name=name_field_oui,value="0")
    embed.add_field(name=name_field_non,value="0")
    bot_message = await ctx.send(embed = embed)
    await bot_message.add_reaction(emoji_oui)
    await bot_message.add_reaction(emoji_non)




bot.run("Your token here")