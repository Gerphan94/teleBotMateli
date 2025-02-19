from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import random, os
from datetime import datetime, timedelta

# Replace this with your bot token from BotFather
TOKEN = "7549783070:AAHkCFj56yau4NMQi4hXyEt9havQP94Bnsw"
IMAGE_FOLDER = 'img/'
# Start command
async def start(update: Update, context):
    user = update.effective_user  # Get user info
    await update.message.reply_text(f"Xin chào {user.first_name}!")
    await update.message.reply_text(f"chat '/image' để xem ảnh nhé")
    await update.message.reply_text(f"chat '/xsmn' lấy xổ số dự đoán nhé")

# Echo message handler
async def echo(update: Update, context):
    user_text = update.message.text
    await update.message.reply_text(f"You said: {user_text}")
    
async def send_xsmn(update: Update, context):
    tomorrow = datetime.now() + timedelta(days=1)
    formatted_tomorrow = tomorrow.strftime("%d/%m/%Y")
    randomso = random.randint(1,100)
    await update.message.reply_text(f"{formatted_tomorrow} số {randomso}")
    
async def send_image(update: Update, context):
    chat_id = update.message.chat_id
    randomnum = random.randint(1, 3)
    image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith((".jpg", ".png", ".jpeg"))]
    
    if not image_files:
        await update.message.reply_text("No images found in the folder!")
        return

    random_image = random.choice(image_files)
    image_path = os.path.join(IMAGE_FOLDER, random_image)

    with open(image_path, "rb") as photo:
        await context.bot.send_photo(chat_id=chat_id, photo=photo)

def main():
    app = Application.builder().token(TOKEN).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("image", send_image))
    app.add_handler(CommandHandler("xsmn", send_xsmn))

    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
