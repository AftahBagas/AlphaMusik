from telethon import Client, filters
from telethon.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIVxGC-q27I1NoiCYx7UtrijASqOaycAAKJAgACXbvgVaglLqi7A0crHwQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Alfareza](https://t.me/kanjengingsun).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📩 Contact Me 📩", url="https://t.me/kanjengingsun")
                ],[
                    InlineKeyboardButton(
                        "🌀 Instagram", url="https://www.instagram.com/aftahbagas"
                    ),     
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/VcgMusicGroup"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/VcgChannelSupport"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/AlphaaMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/VcgChannelSupport")
                ]
            ]
        )
   )


