import discord
from discord.ext import commands
import datetime


class ModMail(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        mod_channel = self.bot.get_channel(int(self.bot.mod_mail_channel))
        if message.guild is None and not message.author.bot:

            ts = datetime.datetime.now().timestamp()
            embed = discord.Embed(title=f":e_mail: **New DM to Bot**", colour=discord.Colour.red(),
                                  timestamp=datetime.datetime.utcfromtimestamp(ts))
            embed.add_field(name="__Message from:__", value=message.author, inline=False)
            embed.add_field(name="__Message__", value=message.content, inline=False)
            message = await mod_channel.send(content=message.author.mention, embed=embed)
            check_mark = '\N{WHITE HEAVY CHECK MARK}'
            cross_mark = '\N{CROSS MARK}'
            await message.add_reaction(check_mark)
            await message.add_reaction(cross_mark)


        if message.content.startswith("!help"):
            embed = discord.Embed(title=f"Set Up Instructions", description="This bot only contains one command.",
                                  colour=discord.Colour.red())
            embed.add_field(name=f"Setup Command", value=f"Type `!setup <incoming mail channel> <resolved queries channel>`\n"
                                                         f"Where incoming mail channel = the channel where you want to receive DMs\n"
                                                         f"And where the resolved channel is where you want resolved or cancelled "
                                                         f"queries to be sent", inline=False)
            embed.add_field(name="Actions", value=f"A message can be marked as completed using the :white_check_mark: reaction."
                                                  f"A new mail message can be cancelled using the :x: reaction. Both these reactions will send the "
                                                  f"mail to the resolved channel, and mark the status of it as resolved. A resolved query can be opened "
                                                  f"again using the :x: reaction from the resolved channel.", inline=False)
            channel = message.guild.get_channel(message.channel.id)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload)
        mail_channel_id = int(self.bot.mod_mail_channel)
        resolved_channel_id = int(self.bot.resolved_mail_channel)
        guild = self.bot.get_guild(payload.guild_id)

        member = guild.get_member(payload.user_id)
        resolved_channel = guild.get_channel(resolved_channel_id)
        mod_channel = guild.get_channel(mail_channel_id)

        if payload.channel_id == mail_channel_id:
            message = await mod_channel.fetch_message(payload.message_id)
            if message.reactions[0].count == 2:
                if payload.emoji.name == '✅':
                    if payload.user_id != self.bot.user.id:
                        embed = message.embeds[0]
                        embed.add_field(name="Status", value=f"Resolved by {payload.member.name}", inline=False)
                        msg = await resolved_channel.send(embed=embed)

                        cross_mark = '\N{CROSS MARK}'
                        await msg.add_reaction(cross_mark)

                        await message.delete()

            if message.reactions[1].count == 2:
                if payload.emoji.name == '❌':
                    if payload.user_id != self.bot.user.id:
                        embed = message.embeds[0]
                        embed.add_field(name="Status", value=f"Cancelled by {payload.member.name}", inline=False)
                        msg = await resolved_channel.send(embed=embed)

                        cross_mark = '\N{CROSS MARK}'
                        await msg.add_reaction(cross_mark)

                        await message.delete()


        if payload.channel_id == resolved_channel_id:
            message = await resolved_channel.fetch_message(payload.message_id)
            if message.reactions[0].count == 2:
                if payload.emoji.name == '❌':
                    if payload.user_id != self.bot.user.id:
                        embed = message.embeds[0]
                        embed.add_field(name="Status", value=f"Reopened by {payload.member.name}", inline=False)
                        msg = await mod_channel.send(embed=embed)

                        check_mark = '\N{WHITE HEAVY CHECK MARK}'
                        cross_mark = '\N{CROSS MARK}'
                        await msg.add_reaction(check_mark)
                        await msg.add_reaction(cross_mark)

                        await message.delete()


def setup(bot):
    bot.add_cog(ModMail(bot))

