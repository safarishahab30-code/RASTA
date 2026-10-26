# handlers.py
from telegram import Update
from telegram.ext import ContextTypes
from keyboards import get_main_menu_keyboard

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = f"سلام {user.first_name} عزیز!\nبه ربات رستا خوش آمدید. لطفا یکی از گزینه‌های زیر را انتخاب کنید:"
    await update.message.reply_text(welcome_text, reply_markup=get_main_menu_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "profile":
        await query.edit_message_text(text="بخش حساب کاربری (به زودی...)")
    elif query.data == "settings":
        await query.edit_message_text(text="بخش تنظیمات (به زودی...)")
    elif query.data == "help":
        await query.edit_message_text(text="راهنمای ربات رستا: برای شروع دکمه‌ها را فشار دهید.")
