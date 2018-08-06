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

from discord.ext import commands

from bdd import bdd
from config import static_var, config
from extensions.constants import disabled_command
from functions import logs

import logging

from functions.check_permissions import is_command_enabled, is_in_group

import gettext
t = gettext.translation('messages', 'locale', fallback=True)
_ = t.gettext

logger = logging.getLogger(__name__)


class CSGOUser(object):
    def __init__(self, bot):
        self.bot = bot
        logging.info("CSGO plugin loaded")

    @commands.command(pass_context=True)
    async def matchs(self, ctx, *user):
        """Avoir des informations sur les matchs en cours"""
        if not is_command_enabled('matchs'):
            await ctx.send(disabled_command.format(ctx))
            return

        msg = ""
        args = ""
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0}  ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        bdd.db_connect(config.EBOT_HOSTNAME, config.EBOT_PORT, config.EBOT_DBNAME, config.EBOT_USERNAME,
                       config.EBOT_PASSWORD)
        result = bdd.db_select()
        bdd.db_disconnect()
        matchs = []
        status = ""
        for row in result:
            if 1 < int(row['status']) < 13:
                matchs.append(row)
        if not matchs:
            msg = msg + "-> Il n'y a aucun match en cours"
        else:
            msg = msg + "-> Matchs en cours : ```"
            for each_match in matchs:
                if int(each_match['enable']) == 0:
                    status = "Stop"
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
                match = '{0} ({1}) vs {2} ({3})'.format(team_a, each_match['score_a'], team_b,
                                                        each_match['score_b'])
                msg = msg + match
                i = 0
                while i < 70 - (len(match) + 20):
                    msg = msg + ' '
                    i = i + 1
                msg = msg + '{0}({1})\n'.format(static_var.ebot_status[int(each_match['status'])], status)
            msg = msg + "```"
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!matchs",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def connect(self, ctx, *user):
        """Lien pour avoir le connect des matchs"""
        if not is_command_enabled('connect'):
            await ctx.send(disabled_command.format(ctx))
            return
        msg = ""
        args = ""
        link = config.URL_ADMINAFK + 'pages/view_connect.php'
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        msg = msg + "-> Lien des connects des matchs : {0}".format(link)
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!connect",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def bracket(self, ctx, *user):
        """Lien du bracket"""
        if not is_command_enabled('bracket'):
            await ctx.send(disabled_command.format(ctx))
            return

        msg = ""
        args = ""
        link = config.URL_ADMINAFK + 'pages/bracket.php'
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        msg = msg + "-> Lien du bracket : {0}".format(link)
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!bracket",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def participants(self, ctx, *user):
        """Lien des participants"""
        if not is_command_enabled('participants'):
            await ctx.send(disabled_command.format(ctx))
            return

        msg = ""
        args = ""
        link = config.URL_ADMINAFK + 'pages/participants.php'
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        msg = msg + "-> Lien des participants : {0}".format(link)
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!participants",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def report(self, ctx, *user):
        """Avoir des informations pour reporter un(e) joueur/équipe"""
        if not is_command_enabled('report'):
            await ctx.send(disabled_command.format(ctx))
            return

        msg = ""
        args = ""
        link = config.URL_ADMINAFK + 'pages/participants.php'
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = msg + "{0.message.author.mention} ".format(ctx)
        msg = msg + " pour faire une demande de gotv vous devez spécifier le match incriminé ainsi que potentiellement les joueurs incriminés. Suite à cela nous vous donnerons un lien que vous devrez regarder et trouver les ticks que vous trouvez suspects (3 minimums)".format(
            link)
        await self.bot.get_channel(config.GOTV_CHANNEL).send(msg)
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!report",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)

    @commands.command(pass_context=True)
    async def rules(self, ctx, *user):
        """Lien du règlement"""
        if not is_command_enabled('rules'):
            await ctx.send(disabled_command.format(ctx))
            return

        msg = ""
        args = ""
        link = config.RULES
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        msg = msg + "-> Lien du règlement : {0}".format(link)
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!rules",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def ebot(self, ctx, *user):
        """Lien de l'eBot"""
        if not is_command_enabled('ebot'):
            await ctx.send(disabled_command.format(ctx))
            return

        msg = ""
        args = ""
        link = config.URL_EBOT
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        msg = msg + "-> Lien de l'eBot : {0}".format(link)
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!ebot",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        await ctx.send(msg)

    @commands.command(pass_context=True)
    async def gotv(self, ctx, *user):
        """Comment regarder une démo ?"""
        if not is_command_enabled('gotv'):
            await ctx.send(disabled_command.format(ctx))
            return

        msg = ""
        args = ""
        if is_in_group(ctx, config.ADMIN_ROLE) and user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        msg = msg + "Pour regarder une démo :\n 1)Télécharge la démo\n 2)Dézippe la démo grâce à winrar par exemple\n 3)Dépose le fichier <nom>.dem dans un dossier sans accent par exemple ton bureau\n 4)Lance CS:GO\n 5)Appuye simultanément sur `Shift` et `F2`\n 6)Appuye sur Load...\n 7)Sélectionne le fichier <nom>.dem\n 8)Le jeu va lancer la démo"
        embed = logs.create_log(self.bot.user.avatar_url, "", "User ID : {0}".format(ctx.message.author.id),
                                static_var.hex_colors_codes['green'], ctx.message.author.name,
                                ctx.message.author.avatar_url, "Action", "Command used", "Name", "!gotv",
                                "Arguments", args)
        await self.bot.get_channel(config.COMMAND_LOGS).send(embed=embed)
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(CSGOUser(bot))
