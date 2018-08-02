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

# Hex Colors Codes
hex_colors_codes = {
    "black": 0x000000,
    "white": 0xffffff,
    "red": 0xd40c00,
    "blue": 0x526eff,
    "green": 0x32c12c,
    "yellow": 0xffef00,
    "orange": 0xff9a00,
    "brown": 0x7c5547,
    "purple": 0x682cbf,
    "grey": 0x9e9e9e
}

# Status of commands (0 = disable, 1 = enable)
status_commands = {
    "matchs": True,
    "connect": True,
    "bracket": True,
    "participants": True,
    "flipcoin": True,
    "report": True,
    "maps": True,
    "purge": True,
    "rules": True,
    "ebot": True,
    "demo": True,
    "gotv": True,
    "ping": True,
    "mute": True,
    "unmute": True
}

# State of flipcoins
flipcoin = ["face", "pile"]

# eBot status
ebot_status = ["not started", "starting", "warmup knife round", "knife round", "end of the knife round",
               "warmup 1st side", "first side", "warmup 2nd side", "econd side", "warmup overtime", "first side OT",
               "warmup 2nd side OT", "second side OT", "finished", "archived"]

# Active Duty Map Pool csgo
mapool_csgo = ["de_dust2", "de_cache", "de_inferno", "de_train", "de_overpass", "de_mirage", "de_nuke"]
