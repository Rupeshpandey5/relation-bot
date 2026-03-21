from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import os

# ---------------- TRUTH & DARE ---------------- #
TRUTHS = [
    "Sabse bada secret kya hai? 🤫",
    "Group me sabse zyada kaun pasand hai? 😏",
    "Kabhi kisi pe secret crush raha hai? 💘",
    "Pehli baar pyaar kab hua tha? 💕",
    "Last kis se chat ki thi? 📱",
    "Apni love life ek word me describe karo ❤️",
    "Kisi teacher se kabhi daant padi hai? 😅",
    "Exam ke time sabse zyada kya darr lagta hai? 📚",
    "Kabhi cheat kiya hai exam me? 😬",
    "Sabse embarrassing moment kya tha? 😳",
    "Kabhi kisi dost se jhoot bola hai? 🤥",
    "Group me sabse cute kaun lagta hai? 🥰",
    "One-sided love kabhi hua hai? 💔",
    "Late night jagne ka reason kya hota hai? 🌙",
    "Kisi pe abhi bhi crush hai? 😌",
    "Apni weakness kya maante ho? 🫣",
    "College/school ka best moment konsa tha? 🎓",
    "Kabhi kisi message ka screenshot liya hai? 📸",
    "Future me love marriage ya arrange? 💍",
    "Aaj ka mood honestly batao 😇"
]

DARES = [
    "Apna nickname batao 😎",
    "Group me 3 emojis bhejo 🔥😂💯",
    "Apni current feeling ek emoji me batao 😊",
    "Kisi ek member ko tag karke hi bolo 👋",
    "Next message ALL CAPS me likho 🗣",
    "Apna favourite song ka naam batao 🎵",
    "Kisi ko group me compliment do 💐",
    "Apni crush type describe karo 😏",
    "Aaj ka study goal batao 📖",
    "Group me ❤️ emoji bhejo",
    "Apna dream job batao 💼",
    "Last used emoji bhejo 😄",
    "Kisi ek word me apna nature batao 🌸",
    "Apna favourite movie ya web series batao 🎬",
    "Aaj ka mood ek sticker me bhejo 🧠",
    "Apni height ka guess batao 📏",
    "Apni favourite food ka naam likho 🍕",
    "Kisi ek member ke liye positive line likho ✨",
    "Apna favourite subject batao 📘",
    "Aaj ka time batao jab uthe the ⏰"
]

RELATIONS = [
    "🤝 Besties", "🖤 Toxic & Loyal", "😈 Devil & Angel",
    "👑 King & Killer Queen", "🐍 Snake & Charmer", "⚡ Thunder & Lightning",
    "😎 Boss & Queen", "🤪 Drama King & Queen", "🔥 Fire & Spark",
    "🐒 Monkey & Banana", "🍕 Pizza & Coke", "🎧 DJ & Listener",
    "💕 Love Birds", "💖 Soulmates", "💘 Heartbeat Duo",
    "💞 Forever Pair", "🌹 Rose & Thorn", "🌙 Moon & Star",
    "☀️ Sun & Sunshine", "Best Friends Forever 🤝", "Chill Buddy 😎",
    "Lucky Pair 🍀", "Study Partners 📚", "College Buddies 🎓",
    "Secret Supporters 🤫", "Power Duo 💪", "Dream Team 🌈"
]

# ---------------- COMMAND FUNCTIONS ---------------- #
def truth(update: Update, context: CallbackContext):
    update.message.reply_text(f"🧐 Truth:\n\n{random.choice(TRUTHS)}")

def dare(update: Update, context: CallbackContext):
    update.message.reply_text(f"🔥 Dare:\n\n{random.choice(DARES)}")

def relation(update: Update, context: CallbackContext):
    chat = update.effective_chat
    if chat.type not in ["group", "supergroup"]:
        update.message.reply_text("Ye command sirf group me kaam karti hai ❌")
        return

    admins = context.bot.get_chat_administrators(chat.id)
    users = [admin.user for admin in admins]
    if len(users) < 2:
        update.message.reply_text("Kam se kam 2 admin hone chahiye 😅")
        return

    u1, u2 = random.sample(users, 2)
    relation_name = random.choice(RELATIONS)
    msg = f"💞 Random Relation Found! 💞\n\n👤 {u1.first_name} 🤝 {u2.first_name}\n🔗 Relation: {relation_name}"
    update.message.reply_text(msg)

def pair(update: Update, context: CallbackContext):
    chat = update.effective_chat
    if chat.type not in ["group", "supergroup"]:
        update.message.reply_text("Ye command sirf group me kaam karti hai ❌")
        return

    admins = context.bot.get_chat_administrators(chat.id)
    users = [admin.user for admin in admins]
    if len(users) < 2:
        update.message.reply_text("Kam se kam 2 admin hone chahiye 😅")
        return

    u1, u2 = random.sample(users, 2)
    pair_names = [
        "🔥 Fire & Spark","🌙 Moon & Star","😎 Boss & Queen",
        "💘 Crush Couple","✨ Golden Duo","👑 King & Queen",
        "💞 Dil & Dhadkan","🫶 Bestie Pair","🤝 Besties"
    ]
    pair_name = random.choice(pair_names)
    msg = f"💘 Special Pair 💘\n\n{u1.first_name} ❤️ {u2.first_name}\n\n✨ {pair_name}"
    update.message.reply_text(msg)

# ---------------- MAIN ---------------- #
TOKEN = os.getenv("TOKEN")
if not TOKEN or len(TOKEN.split(":")) != 2:
    raise ValueError("❌ Invalid TOKEN! Make sure you use the correct Telegram Bot Token.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Add command handlers
dp.add_handler(CommandHandler("truth", truth))
dp.add_handler(CommandHandler("dare", dare))
dp.add_handler(CommandHandler("relation", relation))
dp.add_handler(CommandHandler("pair", pair))

print("🤖 Bot is running...")
updater.start_polling()
updater.idle()