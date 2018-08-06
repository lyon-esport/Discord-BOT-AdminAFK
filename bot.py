from datetime import datetime

import discord
from babel.dates import format_datetime
from discord import User
from discord.ext import commands

import logging

from config import config, hex_colors_codes

logger = logging.getLogger(__name__)


class AdminAFKBot(commands.Bot):
    async def log(self, title: str, description: str, colour: str, user: User, *args, **kwargs):

        # def create_log(bot_avatar_url, title, description, colour, member_name, member_icon, field_name, field_value,
        #                field_name2, field_value2, field_name3, field_value3):
        logger.info("Log command! %s", args)
        now = format_datetime(datetime.now())
        embed = discord.Embed(title=title, description=description, colour=hex_colors_codes[colour])
        embed.set_author(name=user.name, icon_url=user.avatar_url)
        embed.set_footer(text='Discord BOT AdminAFK | Copyright © Lyon e-Sport 2018', icon_url=self.user.avatar_url)
        if not len(args) % 2 == 0:
            logger.error("Error to few arguments")
        args_length = int(len(args) / 2)
        for i in range(args_length):
            embed.add_field(name=args[0+(i*2)], value=args[1+(i*2)])
            # Add date field on the first loop
            if i == 0:
                embed.add_field(name='Date', value=now)
        await self.get_channel(config.COMMAND_LOGS).send(embed=embed)

