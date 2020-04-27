import discord
from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

@bot.event
async def on_reaction_add(reaction,user):
    if reaction.message.author == bot.user and user != bot.user:
        if reaction.emoji == "👍" or reaction.emoji == "👎":
            current_embed = reaction.message.embeds[0]
            current_fields = current_embed.fields
            for field in current_fields:
                if field.name == "Oui :" and reaction.emoji == "👍":
                    current_embed.set_field_at(current_fields.index(field), name = field.name, value = field.value + "\n"+user.name)
                if field.name == "Non :" and reaction.emoji == "👎":
                    current_embed.set_field_at(current_fields.index(field), name = field.name, value = field.value + "\n"+user.name)
            await reaction.message.edit(embed = current_embed)


@bot.command()
async def compris(ctx):
    embed = discord.Embed()
    embed.title = "As-tu compris?"
    embed.color = discord.Colour.blue()
    embed.add_field(name="Oui :",value="👍")
    embed.add_field(name="Non :",value="👎")
    bot_message = await ctx.send(embed = embed)
    await bot_message.add_reaction("👍")
    await bot_message.add_reaction("👎")




bot.run("Your token here")
