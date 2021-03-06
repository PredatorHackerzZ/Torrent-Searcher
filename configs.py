# (c) @PredatorHackerzZ

import os


class Config(object):
    SESSION_NAME = os.environ.get("SESSION_NAME")
    API_ID = int(os.environ.get("API_ID", 12345678))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))

    ABOUT_BOT = """<b>
𝐓𝐡𝐢𝐬 𝐢𝐬 𝐀 𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐁𝐨𝐭𝐋𝐢𝐬𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 𝐎𝐟 @TheTeleRoid 𝐀𝐧𝐝 𝐒𝐨𝐦𝐞 𝐎𝐭𝐡𝐞𝐫 𝐁𝐨𝐭𝐬 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐎𝐧 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦.

🤖 𝗠𝘆 𝗡𝗮𝗺𝗲: <a href='https://t.me/TeleRoid_TorrentSearch_Bot'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝_𝐓𝐨𝐫𝐫𝐞𝐧𝐭𝐒𝐞𝐚𝐫𝐜𝐡_𝐁𝐨𝐭</a>

📜 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲: <a href='https://www.python.org'>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 𝗟𝗶𝗯𝗿𝗮𝗿𝘆: <a href='https://docs.pyrogram.org'>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

📡 𝗛𝗼𝘀𝘁𝗲𝗱 𝗼𝗻: <a href='https://heroku.com'>𝐇𝐞𝐫𝐨𝐤𝐮</a>

👨‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: <a href='https://t.me/PredatorHackerzZ'>@𝐏𝐫𝐞𝐝𝐚𝐭𝐨𝐫𝐇𝐚𝐜𝐤𝐞𝐫𝐳𝐙</a>

🌐 𝗚𝗶𝘁𝗵𝘂𝗕 𝗥𝗲𝗽𝗼: <a href='https://github.com/PredatorHackerzZ'>𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞</a>

👥 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽: <a href='https://t.me/teleroid14'>𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭</a>

📢 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹: <a href='https://t.me/teleroidgroup'>𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝 𝐔𝐩𝐝𝐚𝐭𝐞𝐬</a></b>
"""
    
    HOME_TEXT = """
<b>𝐇𝐞𝐲!, {}, 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐓𝐨𝐫𝐫𝐞𝐧𝐭 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 <a href='https://t.me/TeleRoid_TorrentSearch_Bot'>@𝐓𝐞𝐥𝐞𝐑𝐨𝐢𝐝_𝐓𝐨𝐫𝐫𝐞𝐧𝐭𝐒𝐞𝐚𝐫𝐜𝐡_𝐁𝐨𝐭</a>.

𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 : @TeamTeleRoid

           𝐄𝐯𝐞𝐫𝐲𝐎𝐧𝐞 𝐈𝐧 𝐓𝐡𝐢𝐬 𝐉𝐨𝐮𝐫𝐧𝐞𝐲.</b>
"""
