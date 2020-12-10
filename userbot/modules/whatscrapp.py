"""Syntax: .whatscrapp as reply to a message copied from @WhatsCRApp"""

import logging

from userbot import bot
from userbot.util import admin_cmd, register

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


@bot.on(admin_cmd(pattern="whatscrapp"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        reply_to_id = event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "**")
        the_real_message = the_real_message.replace("_", "__")
        await event.edit(the_real_message)
    else:
        await event.edit(
            "Reply to a message with `.whatscrapp` "
            "to format @WhatsCRApp messages to @Telegram"
        )