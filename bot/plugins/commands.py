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
    update_channel = "@minnal_kurup_murali"
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
                    [ InlineKeyboardButton(text=" ⭕JOIN OUR CHANNEL⭕ ", url=f"https://t.me/minnal_kurup_murali")]
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
                caption = f"📁 <b>Name:</b>\n<code>{file_name}</code>\n<b>━━━━━━━━━━━━━━━━━━━━━\n𝚃𝚑𝚊𝚗𝚔 𝚢𝚘𝚞 𝚏𝚘𝚛 𝚞𝚜𝚒𝚗𝚐 𝚘𝚞𝚛 𝚜𝚎𝚛𝚟𝚒𝚌𝚎 ❣\n 𝚙𝚕𝚎𝚊𝚜𝚎 𝚜𝚑𝚊𝚛𝚎 𝚘𝚞𝚛 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 / 𝚐𝚛𝚘𝚞𝚙 𝚕𝚒𝚗𝚔 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚏𝚛𝚒𝚎𝚗𝚍𝚜.\n━━━━━━━━━━━━━━━━━━━━━\n𝗠𝗼𝘃𝗶𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹: https://t.me/joinchat/MkxtxaJhFHYxZTg1\n𝗦𝗲𝗿𝗶𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹: https://t.me/joinchat/WQNEfDIqGDpkYzcx\n𝗠𝗼𝘃𝗶𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗚𝗿𝗼𝘂𝗽:\nhttps://t.me/joinchat/K2o-tUzqY4FjOWRl</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Movie Request Group', url="https://t.me/mallu_movies_group2"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🎁 Share 🎁', url='https://t.me/share/url?url=%E0%B4%AA%E0%B5%81%E0%B4%A4%E0%B4%BF%E0%B4%AF%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%95%E0%B5%BE%20%E0%B4%9F%E0%B5%86%E0%B4%B2%E0%B4%97%E0%B5%8D%E0%B4%B0%E0%B4%BE%E0%B4%82%20%E0%B4%87%E0%B4%B1%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%81%E0%B4%AE%E0%B5%8D%E0%B4%AA%E0%B5%8B%E0%B5%BE%20%E0%B4%A4%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%86%20%E0%B4%A8%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B4%BF%E0%B4%AB%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%87%E0%B4%B7%E0%B5%BB%20%E0%B4%B2%E0%B4%AD%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%B5%E0%B4%BE%E0%B5%BB%20%E0%B4%A4%E0%B4%BE%E0%B4%B4%E0%B5%86%20%E0%B4%95%E0%B4%BE%E0%B4%A3%E0%B5%81%E0%B4%A8%E0%B5%8D%E0%B4%A8%20%E0%B4%9A%E0%B4%BE%E0%B4%A8%E0%B4%B2%E0%B4%BF%E0%B5%BD%20%E0%B4%9C%E0%B5%8B%E0%B4%AF%E0%B4%BF%E0%B5%BB%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%AF%E0%B5%81%E0%B4%95%20%F0%9F%A5%B3%0A%E2%9C%85%20https%3A%2F%2Ft.me%2Fjoinchat%2FMkxtxaJhFHYxZTg1%20%0A%0A%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%20%E0%B4%8F%E0%B4%A4%E0%B5%81%E0%B4%AE%E0%B4%BE%E0%B4%AF%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%86%F0%9F%A4%B7%E2%80%8D%E2%99%82.%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20%E0%B4%85%E0%B4%9F%E0%B4%BF%E0%B4%9A%E0%B5%8D%E0%B4%9A%E0%B4%BE%E0%B5%BD%20%E0%B4%85%E0%B4%AA%E0%B5%8D%E0%B4%AA%E0%B5%8B%E0%B5%BE%E0%B4%A4%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%86%20%E0%B4%B2%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%95%E0%B5%8D%20%E0%B4%B2%E0%B4%AD%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%A8%E0%B5%8D%E0%B4%A8%20Group%F0%9F%98%8D%F0%9F%98%8D%0A%E2%9C%85%20https%3A%2F%2Ft.me%2Fjoinchat%2FK2o-tUzqY4FjOWRl'),
    ],[
                       InlineKeyboardButton('Movies', url='https://t.me/joinchat/MkxtxaJhFHYxZTg1'),
                       InlineKeyboardButton('Series', url ='https://t.me/joinchat/WQNEfDIqGDpkYzcx')
    ],[
                       InlineKeyboardButton('🔍 Movie Request Group🔎', url ='https://t.me/joinchat/K2o-tUzqY4FjOWRl')
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
        InlineKeyboardButton('Home ⚡', callback_data='start'),
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
        InlineKeyboardButton('Home ⚡', callback_data='start'),
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
