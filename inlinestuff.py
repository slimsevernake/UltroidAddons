#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# .tweet made for ultroid

# .uta ported from Dark-Cobra

"""
✘ Commands Available -

• `{i}uta <search query>`
    Inline song search and downloader.

• `{i}honka <text>`
    make stickers with @honka_says_bot.

• `{i}tweet <text>`
    make twitter posts.

• `{i}quote <search query>`
    quote search via @GoodQuoteBot.

"""

import random

from plugins.stickertools import deEmojify
from telethon.errors import (ChatSendInlineForbiddenError,
                             ChatSendStickersForbiddenError)

from . import *


@ultroid_cmd(pattern="tweet ?(.*)")
async def tweet(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if text is None:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await ultroid_bot.inline_query("twitterstatusbot", text)
        await results[0].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ultroid_cmd(pattern="honka ?(.*)")
async def honkasays(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give Me Some Text !`")
    try:
        if not text.endswith("."):
            text = text + "."
        results = await ultroid_bot.inline_query("honka_says_bot", text)
        await results[2].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ultroid_cmd(pattern="quote ?(.*)")
async def quote(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    try:
        results = await ultroid_bot.inline_query("goodquotebot", text)
        if len(results) == 1:
            num = 0
        else:
            num = random.randrange(0, len(results) - 1)
        await results[num].click(
            e.chat_id,
            silent=True,
            hide_via=True,
        )
        await wai.delete()
    except ChatSendInlineForbiddenError:
        await wai.edit("`Boss ! I cant use inline things here...`")
    except ChatSendStickersForbiddenError:
        await wai.edit("Sorry boss, I can't send Sticker Here !!")


@ultroid_cmd(pattern="uta ?(.*)")
async def nope(doit):
    ok = doit.pattern_match.group(1)
    a = await eor(doit, "`Processing...`")
    if not ok:
        if doit.is_reply:
            (await doit.get_reply_message()).message
        else:
            return await eor(
                doit,
                "`Sir please give some query to search and download it for you..!`",
            )
    sticcers = await ultroid_bot.inline_query("Lybot", f"{(deEmojify(ok))}")
    try:
        await sticcers[0].click(
            doit.chat_id,
            reply_to=doit.reply_to_msg_id,
            silent=True if doit.is_reply else False,
            hide_via=True,
        )
        await a.delete()
    except ChatSendInlineForbiddenError:
        await eor(doit, "`Boss ! I cant use inline things here...`")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
