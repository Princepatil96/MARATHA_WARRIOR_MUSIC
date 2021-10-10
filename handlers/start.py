from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2




 






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
      await message.reply_text("""**
      reply_markup=InlineKeyboardMarkup(
            [
                [
                
           
                ]
            ]
        )
   )


