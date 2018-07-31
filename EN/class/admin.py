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

import sys
import discord
from discord.ext import commands
import random
import time

sys.path.append('../')
sys.path.append('../config/')
sys.path.append('../functions/')

import config
import static_var
import check_permissions
import logs

class Admin():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def maps(self, ctx, nb_round :int):
        """Generate 1 to 7 rounds with random maps"""
        if static_var.status_commands['maps'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                if nb_round < 8 and nb_round >0:
                    maps = random.sample(static_var.mapool_csgo, nb_round)
                    msg = '@here Maps of the tournaments : ```'
                    for i in range(nb_round):
                        msg = msg + "Round {0} : {1}\n".format(i+1, maps[i])
                    msg = msg + "```"
                    await self.bot.get_channel(config.ANNOUNCEMENT).send(msg)
                else:
                    msg = 'You need to select a number in the range of [1;7]'
                    emoji = "<:loudspeaker:473169555557187584>"
                    embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!maps", "Arguments", "{0}".format(nb_round))
                    await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
            else:
                msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        else:
            msg = "{0.message.author.mention} this command is disabled".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def flipcoin(self, ctx, *user):
        """Start a flipcoin (heads/tails)"""
        if static_var.status_commands['flipcoin'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                msg = ""
                args = ""
                if user:
                    for each_user in user:
                        msg = msg + "{0} ".format(each_user)
                    args = msg
                else:
                    msg = "{0.message.author.mention} ".format(ctx)
                choice = random.choice(static_var.flipcoin)
                msg = msg + "-> {0}".format(choice)
                emoji = "<:loudspeaker:473169555557187584>"
                embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!flipcoin", "Arguments", args)
                await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
            else:
                msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        else:
            msg = "{0.message.author.mention} this command is disabled".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def demo(self, ctx, demo_id :int, *user):
        """Generate an URL for download a demo on eBot"""
        if static_var.status_commands['demo'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                msg = ""
                args = ""
                if user:
                    for each_user in user:
                        msg = msg + "{0} ".format(each_user)
                    args = msg
                else:
                    msg = "{0.message.author.mention} ".format(ctx)
                link = '{0}matchs/demo/{1}'.format(config.URL_EBOT, demo_id)
                msg = msg + "the download link is available here -> {0} from now on you have 10 minutes to give us the suspicious ticks (3 minimums) after this time the request will be automatically refused".format(link)
                await self.bot.get_channel(config.GOTV_CHANNEL).send(msg)
                emoji = "<:loudspeaker:473169555557187584>"
                embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!demo", "Arguments", args)
                await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
            else:
                msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        else:
            msg = "{0.message.author.mention} this command is disabled".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def enable(self, ctx, command :str):
        """Enable command"""
        if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
            if command in static_var.status_commands:
                static_var.status_commands[command] = "1"
                msg = '{0.message.author.mention} -> Command !{1} has been enabled'.format(ctx, command)
            else:
                msg= '{0.message.author.mention} -> Command !{1} not found'.format(ctx, command)
            emoji = "<:loudspeaker:473169555557187584>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!enable", "Argument", command)
            await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        else:
            msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def disable(self, ctx, command :str):
        """Disable command"""
        if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
            if command in static_var.status_commands:
                static_var.status_commands[command] = "0"
                msg = '{0.message.author.mention} -> Command !{1} has been disabled'.format(ctx, command)
            else:
                msg= '{0.message.author.mention} -> Command !{1} not found'.format(ctx, command)
            emoji = "<:loudspeaker:473169555557187584>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!disable", "Argument", command)
            await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        else:
            msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def status(self, ctx, command :str):
        """Status of a command"""
        if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
            if command == 'enable' or command == 'disable' or command == 'status':
                msg = '{0.message.author.mention} -> Command !enable, !disable and !status are always enable'.format(ctx)
            else:
                try:
                    if static_var.status_commands[command] == "0":
                        msg = '{0.message.author.mention} -> Command !{1} is disable'.format(ctx, command)
                    elif static_var.status_commands[command] == "1":
                        msg = '{0.message.author.mention} -> Command !{1} is enable'.format(ctx, command)
                except KeyError:
                    msg = '{0.message.author.mention} -> Command !{1} not found'.format(ctx, command)
            emoji = "<:loudspeaker:473169555557187584>"
            embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!status", "Argument", command)
            await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        else:
            msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def purge(self, ctx, number :int):
        """Purge messages"""
        if static_var.status_commands['purge'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                if number < 100 and number > 1:
                    await ctx.channel.purge(limit=int(number+1))
                else:
                    msg = "{0.message.author.mention} -> AdminAFK can only delete messages in the range of [2, 100]".format(ctx)
                    await ctx.send(msg)
                emoji = "<:loudspeaker:473169555557187584>"
                embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!purge", "Argument", "{0}".format(number))
                await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
            else:
                msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
                await ctx.send(msg)
        else:
            msg = "{0.message.author.mention} this command is disabled".format(ctx)
            await ctx.send(msg)

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Test bot connectivity"""
        if static_var.status_commands['ping'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                channel = ctx.message.channel
                t1 = time.perf_counter()
                async with ctx.typing():
                    pass
                t2 = time.perf_counter()
                msg = 'Pong: {}ms !'.format(round((t2-t1)*1000))
                emoji = "<:loudspeaker:473169555557187584>"
                embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!ping", "", "", "")
                await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
            else:
                msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        else:
            msg = "{0.message.author.mention} this command is disabled".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def mute(self, ctx, member):
        """Mute a user"""
        if static_var.status_commands['mute'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                role = discord.utils.get(member.guild.roles, name=config.MUTED_ROLE)
                if role in member.roles:
                    msg="{0.mention} is already muted !".format(member)
                else:
                    await member.add_roles(role)
                    msg="{0.mention} was muted by {1.message.author.mention} !".format(member, ctx)
                emoji = "<:loudspeaker:473169555557187584>"
                embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!mute", "Arguments", member.mention)
                await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
            else:
                msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        else:
            msg = "{0.message.author.mention} this command is disabled".format(ctx)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def unmute(self, ctx, member):
        """Unmute a user"""
        if static_var.status_commands['unmute'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                role = discord.utils.get(member.guild.roles, name=config.MUTED_ROLE)
                if role in member.roles:
                    await member.remove_roles(role)
                    msg="{0.mention} was unmuted by {1.message.author.mention} !".format(member, ctx)
                else:
                    msg="{0.mention} wasn't muted !".format(member)
                emoji = "<:loudspeaker:473169555557187584>"
                embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id), static_var.hex_colors_codes['green'], ctx.message.author.name, ctx.message.author.avatar_url, "Action", "Command used", "Name", "!unmute", "Arguments", member.mention)
                await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
            else:
                msg = "{0.message.author.mention} this command is reserved for admins".format(ctx)
        else:
            msg = "{0.message.author.mention} this command is disabled".format(ctx)
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(Admin(bot))
