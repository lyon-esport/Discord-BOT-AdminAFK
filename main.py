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
from datetime import datetime
from babel.dates import format_date, format_datetime, format_time
from discord import User

from bot import AdminAFKBot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import gettext
gettext.install('messages', 'locale')
t = gettext.translation('messages', 'locale', fallback=True)
_ = t.gettext

import discord
from discord.ext import commands

import config
from functions import check_permissions

description = '''Discord BOT AdminAFK is published under license CeCILL v2.1
Copyright © Lyon e-Sport 2018
by Ludovic « -MoNsTeRRR » Ortega

List of available commands :'''

# this specifies what extensions to load when the bot starts up
startup_extensions = [
    "extensions.CSGO_user",  # CSGO commands (round, flip...)
    "extensions.admin",      # Admin commands (mute, unmute...)
    "extensions.handler_event"
]


bot = AdminAFKBot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='AdminAFK by -MoNsTeRRR', type=0))
    logger.info("Logged as: %s (%s)", bot.user.name, bot.user.id)


@bot.command(hidden=True)
@commands.check(check_permissions.is_bot)
async def load(extension_name: str):
    """Charger une extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say(_("{} loaded.").format(extension_name))


@bot.command(hidden=True)
@commands.check(check_permissions.is_bot)
async def unload(extension_name: str):
    """Retirer une extension"""
    bot.unload_extension(extension_name)
    await bot.say(_("{} removed.").format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            logger.error("Can't load extension %s: %s", extension, exc)

bot.run(config.TOKEN)
