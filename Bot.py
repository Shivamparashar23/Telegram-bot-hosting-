import telegram
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

bot_token = '8121617099:AAEElu6a7F3JeSLJBKT7emtl5hg6tcWv8JM'
github_url = 'YOUR_GITHUB_PAGES_URL'  # अपनी GitHub Pages URL यहाँ डालें

async def start(update, context):
    keyboard = [[InlineKeyboardButton("Open HTML", url=github_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Click the button to open HTML file.", reply_markup=reply_markup)

async def main():
    application = telegram.ApplicationBuilder().token(bot_token).build()
    application.add_handler(telegram.CommandHandler("start", start))
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
