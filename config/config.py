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

##############################
########## Discord ###########
##############################

ADMIN_ROLE = []      # Name of admin roles

MUTED_ROLE = ''      # Name of muted role

GOTV_CHANNEL = ""    # ID of the channel on discord
ANNOUNCEMENT = ""    # ID of the channel on discord

GENERAL_LOGS = ""    # ID of the channel on discord
COMMAND_LOGS = ""    # ID of the channel on discord

TOKEN = ''           # Token of discord BOT

##############################
############ eBot ############
##############################

URL_EBOT = ''        # Base url of eBot

EBOT_HOSTNAME = ''   # Hostname of eBot Database
EBOT_PORT = ''       # Port of eBot Database
EBOT_DBNAME = ''     # Database name of eBot Database
EBOT_USERNAME = ''   # Username of eBot Database
EBOT_PASSWORD = ''   # Password of eBot Database

##############################
######### AdminAFK ###########
##############################

URL_ADMINAFK = ''  # Base url of AdminAFK

##############################
########### Other ############
##############################

RULES = ''  # Link to the rules of the tournament
