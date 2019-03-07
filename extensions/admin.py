# ----------------------------------------------------------------------------
# Copyright © Lyon e-Sport, 2018
#
# Contributeur(s):
#     * Ortega Ludovic - ludovic.ortega@lyon-esport.fr
#     * Etienne Guilluy - etienne.guilluy@lyon-esport.fr
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

import logging
import random
import time
from gettext import gettext as _

import discord
from discord.ext import commands

from bot import AdminAFKBot
from config import config, static_var
from extensions.constants import disabled_command, restricted_command
from functions import decorators
from functions.check_permissions import is_command_enabled, is_in_group, is_admin

logger = logging.getLogger(__name__)


class Admin(commands.Cog):
    def __init__(self, bot: AdminAFKBot):
        self.bot = bot
        logging.info("Admin function loaded")

    @commands.command(pass_context=True, brief=_("Generate 1 to 7 rounds with random maps"))
    @decorators.is_admin
    @decorators.is_command_enabled('maps')
    async def maps(self, ctx, nb_round: int):
        """Générer de 1 à 7 rounds avec des cartes aléatoires"""

        if 8 > nb_round > 0:
            maps = random.sample(static_var.mapool_csgo, nb_round)
            msg = '@here Les maps du tournois sont : ```'
            for i in range(nb_round):
                msg = msg + "Round {0} : {1}\n".format(i + 1, maps[i])
            msg = msg + "```"
            await self.bot.get_channel(config.ANNOUNCEMENT).send(msg)
        else:
            msg = 'Merci de sélectionner un nombre dans l\'interval [1;7]'
            await ctx.send(msg)
        await self.bot.log("Maps", "", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!maps",
                           "Argument", "{0}".format(nb_round))

    @commands.command(pass_context=True, brief=_("Flip a coin (head/tail)"))
    @decorators.is_admin
    @decorators.is_command_enabled('flipcoin')
    async def flipcoin(self, ctx, *users):
        """Faire un pile ou face (pile/face)"""

        args = ""
        if users:
            msg = " ".join(users)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)

        choice = random.choice(static_var.flipcoin)
        msg = msg + "-> {0}".format(choice)
        await self.bot.log("Flipcoin", "", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!flipcoin",
                           "Argument", args)
        await ctx.send(msg)

    @commands.command(pass_context=True, brief=_("Generate an URL for downloading a demo"))
    @decorators.is_admin
    @decorators.is_command_enabled('demo')
    async def demo(self, ctx, demo_id: int, *user):
        """Générer un URL pour télécharger une démo"""

        msg = ""
        args = ""
        if user:
            for each_user in user:
                msg = msg + "{0} ".format(each_user)
            args = msg
        else:
            msg = "{0.message.author.mention} ".format(ctx)
        link = '{0}matchs/demo/{1}'.format(config.URL_EBOT, demo_id)
        msg = msg + "le lien de téléchargement est disponible ici -> {0} à partir de maintenant vous avez 10 minutes pour nous donner les ticks suspects (3 minimums) passé ce délai la demande sera automatiquement refusée".format(
            link)
        await self.bot.get_channel(config.GOTV_CHANNEL).send(msg)
        await self.bot.log("Demo command", "", 'green', ctx.message.author,
                           "Action", "Command used",
                           "Name", "!demo",
                           "Arguments", demo_id)

    @commands.command(pass_context=True, brief=_("Activate a command"))
    @decorators.is_admin
    async def enable(self, ctx, command: str):
        """Activer une commande"""

        if command in static_var.status_commands:
            static_var.status_commands[command] = True
            msg = _("{user} -> Command !{command} has been activated").format(user=ctx.message.author.mention, command=command)
        else:
            msg = _("{user} -> Command !{command} doesn't exists").format(user=ctx.message.author.mention, command=command)
        await self.bot.log("Enable", "", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!enable",
                           "Argument", command)
        await ctx.send(msg)

    @commands.command(pass_context=True, brief=_("Disable a command"))
    @decorators.is_admin
    async def disable(self, ctx, command: str):
        """Désactiver une commande"""

        if command in static_var.status_commands:
            static_var.status_commands[command] = False
            msg = _("{user} -> Command !{command} has been deactivated").format(user=ctx.message.author.mention, command=command)
        else:
            msg = _("{user} -> Command !{command} doesn't exists").format(user=ctx.message.author.mention, command=command)
        await self.bot.log("Disable", "", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!disable",
                           "Argument", command)
        await ctx.send(msg)

    @commands.command(pass_context=True, brief=_("Get if an command is enabled or disabled"))
    @decorators.is_admin
    async def status(self, ctx, command: str):
        """Status d'une commande"""

        if command in ['enable', 'disable', 'status']:
            msg = '{0.message.author.mention} -> La commande !enable, !disable et !status sont toujours activées'.format(ctx)
        else:
            if not command in static_var.status_commands:
                msg = _("{0.message.author.mention} -> Command !{1} doesn't exists").format(ctx, command)
            else:
                if is_command_enabled(command):
                    msg = _('{0.message.author.mention} -> Command !{1} is active').format(ctx, command)
                else:
                    msg = _('{0.message.author.mention} -> Command !{1} is disabled').format(ctx, command)

        await self.bot.log("Status", "", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!status",
                           "Argument", command)
        await ctx.send(msg)

    @commands.command(pass_context=True, brief=_("Delete messages from a channel"))
    @decorators.is_admin
    @decorators.is_command_enabled('purge')
    async def purge(self, ctx, number: int):
        """Delete messages from a channel"""

        if 100 > number > 1:
            await ctx.channel.purge(limit=int(number + 1))
        else:
            msg = "{0.message.author.mention} -> AdminAFK ne peut supprimer que des messages dans un intervalle [2, 99]".format(
                ctx)
            await ctx.send(msg)
        await self.bot.log("Purge", "The purge has started, RUUUUN!", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!purge",
                           "Argument", "{0}".format(number))

    @commands.command(pass_context=True, brief=_("Test the connectivity of the bot"))
    @decorators.is_admin
    @decorators.is_command_enabled('ping')
    async def ping(self, ctx):
        """Test the connectivty of the bot

        Sennd a typing notification and measure the acknowledgement time
        """
        if not is_command_enabled('ping'):
            await ctx.send(disabled_command.format(ctx))
            return

        t1 = time.perf_counter()
        async with ctx.typing():
            pass
        t2 = time.perf_counter()
        msg = 'Pong: {}ms !'.format(round((t2 - t1) * 1000))
        await self.bot.log("Ping", "Ping called", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!ping")
        await ctx.send(msg)

    @commands.command(pass_context=True, brief=_("Mute an user"))
    @decorators.is_admin
    @decorators.is_command_enabled('mute')
    async def mute(self, ctx, member :discord.Member):
        """Mute an user"""
        if not is_command_enabled('mute', ):
            await ctx.send(disabled_command.format(ctx))
            return
        if not is_admin(ctx):
            await ctx.send(restricted_command.format(ctx))
            return

        role = discord.utils.get(member.guild.roles, name=config.MUTED_ROLE)
        if role in member.roles:
            msg = "{0.mention} est déjà muté !".format(member)
        else:
            await member.add_roles(role)
            msg = "{0.mention} a été muté par {1.message.author.mention} !".format(member, ctx)
        await self.bot.log("Mute", "Mute called", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!mute",
                           "Arguments", member.mention)
        await ctx.send(msg)

    @commands.command(pass_context=True, brief=_("Unmute an user"))
    @decorators.is_admin
    @decorators.is_command_enabled('unmute')
    async def unmute(self, ctx, member :discord.Member):
        """Unmute an user"""

        role = discord.utils.get(member.guild.roles, name=config.MUTED_ROLE)
        if role in member.roles:
            await member.remove_roles(role)
            msg = "{0.mention} a été démuté par {1.message.author.mention} !".format(member, ctx)
        else:
            msg = "{0.mention} n'était pas muté !".format(member)

        await self.bot.log("Unmute", "Unmute called", "green", ctx.message.author,
                           "Action", "Command used",
                           "Name", "!unmute",
                           "Arguments", member.mention)
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(Admin(bot))
