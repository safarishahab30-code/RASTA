# keyboards.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("👤 حساب کاربری", callback_data="profile")],
        [InlineKeyboardButton("⚙️ تنظیمات", callback_data="settings")],
        [InlineKeyboardButton("❓ راهنما", callback_data="help")]
    ]
    return InlineKeyboardMarkup(keyboard)
