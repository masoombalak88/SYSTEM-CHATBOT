from config import OWNER_USERNAME, SUPPORT_GRP
from nexichat import nexichat
from pyrogram import Client, filters



START = """**
🤖 ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 🚀

📁 ꜱᴜᴘᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
🌍 ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang
⚙️ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot
🔄 ʏᴏᴜ ᴄᴀɴ ᴄʟᴏɴᴇ/ᴍᴀᴋᴇ ᴄʜᴀᴛʙᴏᴛ ʙʏ /clone
🔄 ᴍᴀᴋᴇ ʏᴏᴜʀ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ ʙʏ /idclone

👥 ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : {}
💬 ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ : {}
⏱️ ᴜᴘᴛɪᴍᴇ » {}

╔═════════════════╗
║ ➻ ᴍʏ ʀᴇᴘᴏ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/APNA_SYSTEM) 🎁                
╚═════════════════╝

➲ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩꜱ ᴛᴏ ᴜꜱᴇ ꜰᴇᴀᴛᴜʀᴇꜱ.
**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/ll_KINGDOM_ll).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
"""

TOOLS_DATA_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴛᴏᴏʟꜱ:

➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!
──────────────
➻ /help ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /speedtest ᴄʜᴇᴄᴋ ꜱᴇʀᴠᴇʀ ꜱᴩᴇᴇᴅ
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!\nᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
➻ /shayri ɢᴇᴛ ʀᴀɴᴅᴏᴍ sʜᴀʏʀɪ ғᴏʀ ʏᴏᴜʀ ʟᴏᴠᴇ
──────────────
➻ /link (ɢʀᴏᴜᴩ ɪᴅ) ᴛᴏ ɢᴇᴛ ʟɪɴᴋ ᴏꜰ ɢʀᴏᴜᴩ
➻ /givelink ᴛᴏ ɢᴇᴛ ᴛʜᴀᴛ ɢʀᴏᴜᴩ ʟɪɴᴋ ɪɴ ᴡʜɪᴄʜ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴡʀɪᴛᴛᴇɴ (ᴡʀɪᴛᴇ ɪɴ ɢʀᴏᴜᴩ)
──────────────
➻ ᴜsᴇ /repo ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➲ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩꜱ ᴛᴏ ᴜꜱᴇ ꜰᴇᴀᴛᴜʀᴇꜱ.**
"""

CHATBOT_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʜᴀᴛʙᴏᴛ:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏns ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /ask - ᴀꜱᴋ ᴀɴʏᴛʜɪɴɢ ꜰʀᴏᴍ ᴄʜᴀᴛɢᴩᴛ
──────────────
➻ /lang, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.  
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
➻ /chatlang - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ᴜꜱɪɴɢ ᴄʜᴀᴛ ʟᴀɴɢ ꜰᴏʀ ᴄʜᴀᴛ.
──────────────
➻ /status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏʀ ɴᴏᴛ.
──────────────
➻ /stats - ɢᴇᴛ ʙᴏᴛ ꜱᴛᴀᴛꜱ
──────────────
➻ /clone [ ʙᴏᴛ ᴛᴏᴋᴇɴ ] - ᴛᴏ ᴄʟᴏɴᴇ ʏᴏᴜʀ ʙᴏᴛ.
──────────────
➻ /idclone [ ᴩʏʀᴏɢʀᴀᴍ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ] - ᴛᴏ ᴍᴀᴋᴇ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ.
──────────────
➲ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩꜱ ᴛᴏ ᴜꜱᴇ ꜰᴇᴀᴛᴜʀᴇꜱ.
**"""

SOURCE_READ = f"**ʜᴇʏ, ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ [{nexichat.name}](https://t.me/{nexichat.username}) ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.**\n**ᴘʟᴇᴀsᴇ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ & ɢɪᴠᴇ ᴛʜᴇ sᴛᴀʀ ✯**\n**──────────────────**\n**ʜᴇʀᴇ ɪs ᴛʜᴇ [sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ](https://t.me/EXAMPURRS)**\n**──────────────────**\n**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP}).\n<b>||📡 ᴍᴀᴅᴇ ʙʏ ➪ [˹sʏsᴛᴇᴍ ɴᴇᴛᴡᴏʀᴋ˼](https://t.me/APNA_SYSTEM) 💞**||</b>"

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{nexichat.name}](https://t.me/{nexichat.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{nexichat.name}](https://t.me/{nexichat.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{nexichat.name}](https://t.me/{nexichat.username})**
"""
