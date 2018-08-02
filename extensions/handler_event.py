# ----------------------------------------------------------------------------
# Copyright © Lyon e-Sport, 2018
#
# Contributeur(s):
#     * Ortega Ludovic - ludovic.ortega@lyon-esport.fr
#
#  Ce logiciel, Discord BOT AdminAFK, est un programme informatique servant à administrer
#  et gérer un tournoi CS:GO avec eBot, Toornament et Discord.
#
# Ce logiciel est régi par la licence CeCILL soumise au droit français et
# respectant les principes de diffusion des logiciels libres. Vous pouvez
# utiliser, modifier et/ou redistribuer ce programme sous les conditions
# de la licence CeCILL telle que diffusée par le CEA, le CNRS et l'INRIA
# sur le site "http://www.cecill.info".
#
# En contrepartie de l'accessibilité au code source et des droits de copie,
# de modification et de redistribution accordés par cette licence, il n'est
# offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
# seule une responsabilité restreinte pèse sur l'auteur du programme,  le
# titulaire des droits patrimoniaux et les concédants successifs.
#
# A cet égard  l'attention de l'utilisateur est attirée sur les risques
# associés au chargement,  à l'utilisation,  à la modification et/ou au
# développement et à la reproduction du logiciel par l'utilisateur étant
# donné sa spécificité de logiciel libre, qui peut le rendre complexe à
# manipuler et qui le réserve donc à des développeurs et des professionnels
# avertis possédant  des  connaissances  informatiques approfondies.  Les
# utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
# logiciel à leurs besoins dans des conditions permettant d'assurer la
# sécurité de leurs systèmes et ou de leurs données et, plus généralement,
# à l'utiliser et l'exploiter dans les mêmes conditions de sécurité.
#
# Le fait que vous puissiez accéder à cet en-tête signifie que vous avez
# pris connaissance de la licence CeCILL, et que vous en avez accepté les
# termes.
# ----------------------------------------------------------------------------
import asyncio

import discord

from config import config, static_var
from functions import logs


class Log():
    def __init__(self, bot):
        self.bot = bot

    async def on_member_unban(self, guild, user):
        """Event : user unbanned"""
        await asyncio.sleep(1)
        audit_log_entries = guild.audit_logs(action=discord.AuditLogAction.ban, limit=1)
        async for entry in audit_log_entries:
            emoji = "<:hammer:472142338089549835>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(entry.user.id), static_var.hex_colors_codes['green'], entry.user.name, entry.user.avatar_url, "Action", "{0} User unbanned".format(emoji), "User", user.name, "Content", "The user has been unbanned from the server")
            await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_member_ban(self, guild, user):
        """Event : user banned"""
        await asyncio.sleep(1)
        audit_log_entries = guild.audit_logs(action=discord.AuditLogAction.ban, limit=1)
        async for entry in audit_log_entries:
            emoji = "<:hammer:472142338089549835>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(entry.user.id), static_var.hex_colors_codes['red'], entry.user.name, entry.user.avatar_url, "Action", "{0} User banned".format(emoji), "User", user.name, "Content", "The user has been banned from the server")
            await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_member_join(self, member):
        """Event : user joined the server"""
        emoji = "<:wave:472141177475563542>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(member.id), static_var.hex_colors_codes['green'], member.name, member.avatar_url, "Action", "{0} User state".format(emoji), "Content", "User joined", "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_member_update(self, before, after):
        """Event : user updated"""
        if before.nick != after.nick or before.avatar_url != after.avatar_url or set(before.roles) != set(after.roles):
            title_before = ""
            content_before = ""
            title_after = ""
            content_after = ""
            if before.nick != after.nick:
                title_before = "Old nickname"
                content_before = "{0}".format(before.nick)
                title_after = "New nickname"
                content_after = "{0}".format(after.nick)
            elif before.avatar_url != after.avatar_url:
                title_before = ""
                content_before = ""
                title_after = "New avatar"
                content_after = "{0}".format(after.avatar_url)
            elif set(before.roles) != set(after.roles):
                if len(after.roles) > len(before.roles):
                    diff_role = list(set(after.roles) - set(before.roles))
                    title_before = "User role added to {0}".format(after.name)
                    content_before = "{0}".format(diff_role[0].mention)
                else:
                    diff_role = list(set(before.roles) - set(after.roles))
                    title_before = "User role deleted to {0}".format(after.name)
                    content_before = "{0}".format(diff_role[0].mention)
                title_after = "User role"
                if len(after.roles) == 2:
                    content_after = "None"
                else:
                    for i in range(2, len(after.roles)):
                        content_after = "{0} {1}".format(content_after, after.roles[i].mention)
            emoji = "<:tools:472152893517070346>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(after.id), static_var.hex_colors_codes['orange'], after.name, after.avatar_url, "Action", "{0} User state".format(emoji), title_before, content_before, title_after, content_after)
            await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_member_remove(self, member):
        """Event : user left the server"""
        await asyncio.sleep(1)
        audit_log_entries = member.guild.audit_logs(action=discord.AuditLogAction.ban, limit=1)
        async for entry in audit_log_entries:
            audit_log_entries2 = member.guild.audit_logs(action=discord.AuditLogAction.unban, limit=1)
            async for entry2 in audit_log_entries2:
                if entry.created_at < entry2.created_at:
                    emoji = "<:wave:472141177475563542>"
                    embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(member.id), static_var.hex_colors_codes['red'], member.name, member.avatar_url, "Action", "{0} User state".format(emoji), "Content", "User left", "", "")
                    await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_channel_create(self, channel):
        """Event : channel created"""
        emoji = "<:new:472152627765968936>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['green'], "", "", "Action", "{0} Channel state".format(emoji), "Content", "{0} channel created".format(channel.mention), "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_channel_update(self, before, after):
        """Event : channel updated"""
        emoji = "<:tools:472152893517070346>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['orange'], "", "", "Action", "{0} Channel state".format(emoji), "Content", "{0} channel updated".format(after.mention), "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_channel_delete(self, channel):
        """Event : channel deleted"""
        await asyncio.sleep(1)
        audit_log_entries = channel.guild.audit_logs(action=discord.AuditLogAction.channel_delete, limit=1)
        async for entry in audit_log_entries:
            emoji = "<:x:472152627765968936>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['red'], "", "", "Action", "{0} Channel state".format(emoji), "Content", "#{0} channel deleted".format(entry.before.name), "", "")
            await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_update(self, before, after):
        """Event : server updated"""
        emoji = "<:tools:472152893517070346>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['orange'], "", "", "Action", "{0} Server state".format(emoji), "Content", "{0} server setting updated".format(after.name), "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_role_create(self, role):
        """Event : role created"""
        emoji = "<:new:472152627765968936>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['green'], "", "", "Action", "{0} Role state".format(emoji), "Content", "{0} role created".format(role.mention), "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_role_update(self, before, after):
        """Event : role updated"""
        emoji = "<:tools:472152893517070346>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['orange'], "", "", "Action", "{0} Role state".format(emoji), "Content", "{0} role updated".format(after.mention), "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_role_delete(self, role):
        """Event : role deleted"""
        await asyncio.sleep(1)
        audit_log_entries = role.guild.audit_logs(action=discord.AuditLogAction.role_delete, limit=1)
        async for entry in audit_log_entries:
            emoji = "<:x:472152627765968936>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['red'], "", "", "Action", "{0} Role state".format(emoji), "Content", "@{0} role deleted".format(entry.before.name), "", "")
            await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_guild_emojis_update(self, guild, before, after):
        """Event : emojis updated"""
        emoji = "<:tools:472152893517070346>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "", static_var.hex_colors_codes['red'], "", "", "Action", "{0} Emojis state".format(emoji), "Content", "{0} server emojis updated".format(guild.name), "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_voice_state_update(self, member, before, after):
        """Event : voice state"""
        content = ""
        if before.deaf != after.deaf:
            if after.deaf == True:
                content = content + "Server has turned off his sound"
            else:
                content = content + "Server has turned on his sound"
        if before.self_deaf != after.self_deaf:
            if after.self_deaf == True:
                content = content + "User has turned off his sound"
            else:
                content = content + "User has turned on his sound"
        if before.mute != after.mute:
            if content != "":
                content = content + " and "
            if after.mute == True:
                content = content + "Server has turned off his microphone"
            else:
                content = content + "Server has turned on his microphone"
        if before.self_mute != after.self_mute:
            if content != "":
                content = content + " and "
            if after.self_mute == True:
                content = content + "User has turned off his microphone"
            else:
                content = content + "User has turned on his microphone"
        if before.afk != after.afk:
            if content != "":
                content = content + " and "
            if after.afk == True:
                content = content + "User joined AFK channel {0} from {1} channel".format(after.channel, before.channel)
            else:
                content = content + "User left AFK channel {0} to {1} channel".format(before.channel, after.channel)
        if before.channel != after.channel:
            if content != "":
                content = content + " and "
            if after.channel == None:
                content = "User left voice server from {} channel".format(before.channel)
            elif before.channel == None and after.channel != None:
                content = "User joined voice server on {0} channel".format(after.channel)
            else:
                content = "User joined {0} channel from {1} channel".format(after.channel, before.channel)
        emoji = "<:loud_sound:472137635163406347>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(member.id), static_var.hex_colors_codes['orange'], member.name, member.avatar_url, "Action", "{0} Voice state".format(emoji), "Content", content, "", "")
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_message_edit(self, before, after):
        """Event : message edited"""
        if len(after.content)<220:
            after_content = after.content
        else:
            after_content = after.content[:250]
            after_content = after_content + "..."
        if len(before.content)<220:
            before_content = before.content
        else:
            before_content = before.content[:250]
            before_content = before_content + "..."
        if before.content != after.content:
            emoji = "<:tools:472152893517070346>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(after.author.id), static_var.hex_colors_codes['orange'], after.author, after.author.avatar_url, "Action", "{0} Message edited".format(emoji), "Before", before_content, "After", after_content)
            await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)
        """Event : message pinned"""
        if before.pinned != after.pinned:
            emoji = "<:tools:472152893517070346>"
            if after.pinned == True:
                pinned_state = "Message pinned"
            else:
                pinned_state = "Message unpinned"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(after.author.id), static_var.hex_colors_codes['orange'], after.author, after.author.avatar_url, "Action", "{0} Message state".format(emoji), "State", pinned_state, "Content", after_content)
            await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

    async def on_message_delete(self, message):
        """Event : message deleted"""
        if len(message.content)<220:
            content = message.content
        else:
            content = message.content[:250]
            content = content + "..."
        emoji = "<:warning:472139637142323231>"
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(message.author.id), static_var.hex_colors_codes['red'], message.author.name, message.author.avatar_url, "Action", "{0} Message deleted".format(emoji), "Message information", "Message sent by {0} deleted in {1}".format(message.author.mention, message.channel.mention), "Content", content)
        await self.bot.get_channel(config.GENERAL_LOGS).send(embed=embed)

def setup(bot):
    bot.add_cog(Log(bot))
