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
import discord
from discord.ext import commands
import datetime


def create_log(bot_avatar_url, title, description, colour, member_name, member_icon, field_name, field_value, field_name2, field_value2, field_name3, field_value3):
    now = datetime.datetime.now().strftime('%a %b %d, %Y at %H:%M %p')
    embed = discord.Embed(title=title, description=description, colour=colour)
    embed.set_author(name=member_name, icon_url=member_icon)
    embed.set_footer(text='Discord BOT AdminAFK | Copyright © Lyon e-Sport 2018', icon_url=bot_avatar_url)
    if field_name and field_value:
        embed.add_field(name=field_name, value=field_value)
    embed.add_field(name='Date', value=now)
    if field_name2 and field_value2:
        embed.add_field(name=field_name2, value=field_value2, inline=False)
    if field_name3 and field_value3:
        embed.add_field(name=field_name3, value=field_value3)
    return embed
