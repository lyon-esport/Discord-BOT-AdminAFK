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

import pymysql

import logging
logger = logging.getLogger(__name__)


def db_connect(hostname, port, dbname, username, password):
    global connection
    connection = pymysql.connect(
        host=hostname,
        port=int(port),
        user=username,
        password=password,
        db=dbname,
        charset='utf8',
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor
    )


def db_select():
    sql = """
    SELECT
        matchs.id,
        matchs.team_a_name,
        matchs.team_b_name,
        matchs.score_a,
        matchs.score_b,
        ta.name AS teama_name,
        tb.name AS teamb_name,
        matchs.status,
        matchs.enable
    FROM
        matchs
    LEFT JOIN
        maps
    ON
        maps.match_id = matchs.id
    LEFT JOIN
        teams AS ta
    ON
        ta.id = team_a
    LEFT JOIN
        teams AS tb
    ON
        tb.id = team_b
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    except pymysql.err.InternalError as e:
        code, msg = e.args
        logger.error("Problem during query, code: %s error: %s", code, msg)
    except Exception as e:
        logger.error("Problem during query: %s", e)


def db_disconnect():
    connection.close()
