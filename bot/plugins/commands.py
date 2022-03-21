#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@Movies_Updates0"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="🔊 <b>ഞങ്ങളുടെ 𝙈𝙖𝙞𝙣 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 ജോയിൻ ചെയ്താൽ മാത്രമേ സിനിമ ലഭിക്കുകയുള്ളൂ. 🤷‍♂ \n ചാനലിൽ join ചെയ്തിട്ട് ഒന്നുകൂടി Try ചെയ്യ്. ❤️</b>😁",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" ⭕JOIN OUR CHANNEL⭕ ", url=Translation.MOVIES)]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"📁 <b>Name:</b>\n<code>{file_name}</code>\n<b>━━━━━━━━━━━━━━━━━━━━━\n𝚃𝚑𝚊𝚗𝚔 𝚢𝚘𝚞 𝚏𝚘𝚛 𝚞𝚜𝚒𝚗𝚐 𝚘𝚞𝚛 𝚜𝚎𝚛𝚟𝚒𝚌𝚎 ❣\n 𝚙𝚕𝚎𝚊𝚜𝚎 𝚜𝚑𝚊𝚛𝚎 𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 / 𝚐𝚛𝚘𝚞𝚙 𝚕𝚒𝚗𝚔 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚏𝚛𝚒𝚎𝚗𝚍𝚜.\n━━━━━━━━━━━━━━━━━━━━━\n𝗠𝗼𝘃𝗶𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹:\n" + Translation.MOVIES + f"\n𝗦𝗲𝗿𝗶𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹:\n" +Translation.SERIES + f"\n𝗠𝗼𝘃𝗶𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗚𝗿𝗼𝘂𝗽:\n" + Translation.GROUP + "</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [[
                       InlineKeyboardButton('🎁 Share 🎁', url=Translation.SHARE),
                     ],[
                       InlineKeyboardButton('Movies', url=Translation.MOVIES),
                       InlineKeyboardButton('Series', url =Translation.SERIES)
                     ],[
                       InlineKeyboardButton('🔍 Movie Request Group🔎', url =Translation.GROUP)
                    ]]
               )
            )
        try:
            await update.send_cached_media(
                chat_id=-1001770753985,
                file_id,
                quote=True,
                caption =Translation.START_TEXT.format(
                update.from_user.first_name),
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [[
                       InlineKeyboardButton('🎁 Share 🎁', url=Translation.SHARE),
                     ],[
                       InlineKeyboardButton('Movies', url=Translation.MOVIES),
                       InlineKeyboardButton('Series', url =Translation.SERIES)
                     ],[
                       InlineKeyboardButton('🔍 Movie Request Group🔎', url =Translation.GROUP)
                    ]]
               )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
                       InlineKeyboardButton('🎁 Share 🎁', url=Translation.SHARE),
    ],[
                       InlineKeyboardButton('Movies', url=Translation.MOVIES),
                       InlineKeyboardButton('Series', url =Translation.SERIES)
    ],[
                       InlineKeyboardButton('🔍 Movie Request Group🔎', url =Translation.GROUP)
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
