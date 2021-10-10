from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/695d103e0ec3d017c6770.jpg")
    await message.reply_text(





        """,

            [
                [
     
            
                  ],[
   
         
                    ),
       
a"
                    )
                ],[ 
           
             
                    )]

  
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**『𝙿𝚁𝙸𝙽_𝚂𝙴𝙲𝙲 𝙼𝚄𝚂𝙸𝙲』 IS ALIVE**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 🔰", url="https://t.me/PRIN_SECC")
                ]
            ]
        )
   )


