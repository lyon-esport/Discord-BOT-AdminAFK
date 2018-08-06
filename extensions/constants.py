# coding=utf-8
# author Etienne G.

import logging

logger = logging.getLogger(__name__)

import gettext
t = gettext.translation('messages', 'locale', fallback=True)
_ = t.gettext

disabled_command = _("{0.message.author.mention} this command is disabled")
restricted_command = _("{0.message.author.mention} this commands is restricted to the admins")