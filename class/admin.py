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

sys.path.append('../')
sys.path.append('../config/')
sys.path.append('../functions/')

import config
import static_var
import check_permissions

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
                    await self.bot.send_message(discord.Object(id=config.ANNOUNCEMENT), msg)
                else:
                    msg = 'You need to select a number in the range of [1;7]'
                    await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def flipcoin(self, ctx, *user):
        """Start a flipcoin (heads/tails)"""
        if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
            if static_var.status_commands['flipcoin'] == "1":
                msg = ""
                if user:
                    for each_user in user:
                        msg = msg + "{0} ".format(each_user)
                else:
                    msg = "{0.message.author.mention} ".format(ctx)
                choice = random.choice(static_var.flipcoin)
                msg = msg + "-> {0}".format(choice)
                await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def demo(self, ctx, demo_id :int, *user):
        """Generate an URL for download a demo on eBot"""
        if static_var.status_commands['demo'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                msg = ""
                if user:
                    for each_user in user:
                        msg = msg + "{0} ".format(each_user)
                else:
                    msg = "{0.message.author.mention} ".format(ctx)
                link = '{0}matchs/demo/{1}'.format(config.URL_EBOT, demo_id)
                msg = msg + "the download link is available here -> {0} from now on you have 10 minutes to give us the suspicious ticks (3 minimums) after this time the request will be automatically refused".format(link)
                await self.bot.send_message(discord.Object(id=config.GOTV_CHANNEL), msg)
    
    @commands.command(pass_context=True)
    async def enable(self, ctx, command):
        """Enable command"""
        if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
            if command in static_var.status_commands:
                static_var.status_commands[command] = "1"
                msg = '{0.message.author.mention} -> Command !{1} has been enabled'.format(ctx, command)
            else:
                msg= '{0.message.author.mention} -> Command !{1} not found'.format(ctx, command)
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def disable(self, ctx, command :str):
        """Disable command"""
        if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
            if command in static_var.status_commands:
                static_var.status_commands[command] = "0"
                msg = '{0.message.author.mention} -> Command !{1} has been disabled'.format(ctx, command)
            else:
                msg= '{0.message.author.mention} -> Command !{1} not found'.format(ctx, command)
            await self.bot.say(msg)

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
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def purge(self, ctx, number :int):
        """Purge messages"""
        if static_var.status_commands['purge'] == "1":
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                if number < 101 and number > 1:
                    mgs = []
                    async for x in self.bot.logs_from(ctx.message.channel, limit = number):
                        mgs.append(x)
                    await self.bot.delete_messages(mgs)
                else:
                    msg = '{0.message.author.mention} -> AdminAFK can only delete messages in the range of [2, 100]'.format(ctx)
                    await self.bot.say(msg)

def setup(bot):
    bot.add_cog(Admin(bot))
