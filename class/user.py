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

sys.path.append('../')
sys.path.append('../config/')
sys.path.append('../bdd/')
sys.path.append('../functions/')

import config
import static_var
import bdd
import check_permissions

class User():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def matchs(self, ctx, *user):
        """Get info about matches on eBot"""
        if static_var.status_commands['matchs'] == "1":
            msg = ""
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = "{0.message.author.mention} ".format(ctx)
            msg = msg + "-> Live matches : ```"
            bdd.db_connect(config.EBOT_HOSTNAME, config.EBOT_PORT, config.EBOT_DBNAME, config.EBOT_USERNAME, config.EBOT_PASSWORD)
            result = bdd.db_select()
            bdd.db_disconnect()
            matchs = []
            status = "";
            for row in result:
                if int(row['status']) > 1 and int(row['status']) < 13:
                    matchs.append(row)
            for each_match in matchs:
                if int(each_match['enable']) == 0:
                     status = "Stopped"
                else:
                      status = "Live"
                if each_match['teama_name'] is None:
                    team_a = each_match['team_a_name']
                else:
                      team_a = each_match['teama_name']
                if each_match['teamb_name'] is None:
                    team_b = each_match['team_b_name']
                else:
                    team_b = each_match['teamb_name']
                match = '{0} ({1}) vs {2} ({3})'.format(team_a, each_match['score_a'], team_b, each_match['score_b'])
                msg = msg + match
                i = 0
                while i < 70 - (len(match)+20):
                    msg = msg + ' '
                    i = i + 1
                msg = msg + '{0}({1})\n'.format(static_var.ebot_status[int(each_match['status'])], status)
            msg = msg + "```"
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def connect(self, ctx, *user):
        """Get the link of connect team"""
        if static_var.status_commands['connect'] == "1":
            msg = ""
            link = config.URL_ADMINAFK +'pages/view_connect.php'
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = "{0.message.author.mention} ".format(ctx)
            msg = msg + "-> Link of connect team : {0}".format(link)
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def bracket(self, ctx, *user):
        """Get the link of bracket"""
        if static_var.status_commands['bracket'] == "1":
            msg = ""
            link = config.URL_ADMINAFK +'pages/bracket.php'
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = "{0.message.author.mention} ".format(ctx)
            msg = msg + "-> Link of bracket : {0}".format(link)
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def participants(self, ctx, *user):
        """Get the link of participants"""
        if static_var.status_commands['participants'] == "1":
            msg = ""
            link = config.URL_ADMINAFK +'pages/participants.php'
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = "{0.message.author.mention} ".format(ctx)
            msg = msg + "-> Link of participants : {0}".format(link)
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def report(self, ctx, *user):
        """Get infos for report a player/team"""
        if static_var.status_commands['report'] == "1":
            msg = "Hello "
            link = config.URL_ADMINAFK +'pages/participants.php'
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = msg + "{0.message.author.mention} ".format(ctx)
            msg = msg + " reply here for make a dispute with the name of your team and the opposant team. Admin Team will give you a link for download the GOTV after that you will have 10 minutes to found ticks (3 minimums).".format(link)
            await self.bot.send_message(discord.Object(id=config.GOTV_CHANNEL), msg)

    @commands.command(pass_context=True)
    async def rules(self, ctx, *user):
        """Get the link of rules"""
        if static_var.status_commands['rules'] == "1":
            msg = ""
            link = config.RULES
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = "{0.message.author.mention} ".format(ctx)
            msg = msg + "-> Link of rules : {0}".format(link)
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def ebot(self, ctx, *user):
        """Get the link of eBot"""
        if static_var.status_commands['ebot'] == "1":
            msg = ""
            link = config.URL_EBOT
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = "{0.message.author.mention} ".format(ctx)
            msg = msg + "-> Link of eBot : {0}".format(link)
            await self.bot.say(msg)

    @commands.command(pass_context=True)
    async def gotv(self, ctx, *user):
        """How to watch a demo ?"""
        if static_var.status_commands['gotv'] == "1":
            msg = ""
            if check_permissions.check_if_it_is_admin(ctx, config.ADMIN_ROLE):
                for each_user in user:
                    msg = msg + "{0} ".format(each_user)
            else:
                msg = "{0.message.author.mention}".format(ctx)
            msg = msg + "To watch a demo :\n 1)Download the démo\n 2)Unzip the demo with winrar for example\n 3)Move the file <nom>.dem in a folder without accent for example on the desktop\n 4)Start CS:GO\n 5)Press simultaneously ```Shift``` and ```F2```\n 6)Press Load...\n 7)Select the file <nom>.dem\n 8)The game will launch the demo"
            await self.bot.say(msg)

def setup(bot):
    bot.add_cog(User(bot))
