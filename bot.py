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
    "Apni love life ek word me describe karo ❤️"
]

DARES = [
    "Apna nickname batao 😎",
    "Group me 3 emojis bhejo 🔥😂💯",
    "Next message ALL CAPS me likho 🗣",
    "Apna favourite song ka naam batao 🎵"
]

RELATIONS = [
    "🤝 Besties", "🖤 Toxic & Loyal", "😈 Devil & Angel",
    "👑 King & Queen", "🔥 Fire & Spark", "💕 Love Birds"
]

# ---------------- FUNCTIONS ---------------- #

def truth(update: Update, context: CallbackContext):
    update.message.reply_text(f"🧐 Truth:\n\n{random.choice(TRUTHS)}")

def dare(update: Update, context: CallbackContext):
    update.message.reply_text(f"🔥 Dare:\n\n{random.choice(DARES)}")

def relation(update: Update, context: CallbackContext):
    chat = update.effective_chat

    if chat.type not in ["group", "supergroup"]:
        update.message.reply_text("Group me use karo ❌")
        return

    admins = context.bot.get_chat_administrators(chat.id)
    users = [admin.user for admin in admins]

    if len(users) < 2:
        update.message.reply_text("2 admin chahiye 😅")
        return

    u1, u2 = random.sample(users, 2)

    msg = (
        f"💞 Relation 💞\n\n"
        f"{u1.first_name} ❤️ {u2.first_name}\n"
        f"{random.choice(RELATIONS)}"
    )

    update.message.reply_text(msg)

def pair(update: Update, context: CallbackContext):
    relation(update, context)

# ---------------- MAIN ---------------- #

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN not set")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("truth", truth))
dp.add_handler(CommandHandler("dare", dare))
dp.add_handler(CommandHandler("relation", relation))
dp.add_handler(CommandHandler("pair", pair))

print("Bot running...")
updater.start_polling()
updater.idle()