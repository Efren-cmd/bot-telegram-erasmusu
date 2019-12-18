
"""
Basic example for a bot that uses inline keyboards.
"""
import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

# Global vars:

SET_LANG = range(1)
global LANG



def start(update, context):

    reply_keyboard = [['ES', 'EN']]
    update.message.reply_text(
    "Please select a language to start. / Por favor selecciona un idioma \
        para comenzar.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return SET_LANG

def menu(update, context):
    reply_keyboard = [['ES', 'EN']]

    update.message.reply_text(
    "Please select a language to start. / Por favor selecciona un idioma \
        para comenzar.",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return SET_LANG


def set_lang(update, context):
    user = update.message.from_user
    logger.info("Language of %s: %s", user.first_name, update.message.text)
    nombre=user.first_name
    if update.message.text == 'EN':
        keyboard = [[InlineKeyboardButton("I’m looking for accommodation (link)",url="https://cutt.ly/CrqHEz8", callback_data='1')],
        [InlineKeyboardButton("I need help with my booking", callback_data='2')],
        [InlineKeyboardButton("I’m a verified user and I need help with my profile", callback_data='3')],
        [InlineKeyboardButton("I’m a non-verified user and I need help with my profile", callback_data='4')],
        [InlineKeyboardButton("I have other inquiries", callback_data='5')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Hi '+nombre+'! What you need?',reply_markup=reply_markup)


    if update.message.text == 'ES':
        keyboard = [[InlineKeyboardButton("Estoy buscando alojamiento (link)",url="https://cutt.ly/CrqHEz8", callback_data='1')],
        [InlineKeyboardButton("Necesito ayuda con mi alojamiento", callback_data='2')],
        [InlineKeyboardButton("Soy un usuario verificado y necesito ayuda con mi perfil", callback_data='3')],
        [InlineKeyboardButton("Soy un usuario no verificado y necesito ayuda con mi perfil", callback_data='4')],
        [InlineKeyboardButton("Tengo otra consulta", callback_data='5')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('¡Hola '+nombre+'! Dinos qué necesitas:',reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    if update.callback_query.data == '1': query.edit_message_text(text="Selected option: 1")
    elif update.callback_query.data == '2': query.edit_message_text(text="Hello. Please write your inquiry to bookings@erasmusu.com and one agent will get in touch with you as soon as possible")
    elif update.callback_query.data == '3': query.edit_message_text(text="Hello. Please write your inquiry to bookings@erasmusu.com and one agent will get in touch with you as soon as possible")
    elif update.callback_query.data == '4': query.edit_message_text(text="Hello. Please write your inquiry to info@erasmusu.com and one agent will get in touch with you as soon as possible")
    elif update.callback_query.data == '5': query.edit_message_text(text="Hello. Please write your inquiry to info@erasmusu.com and one agent will get in touch with you as soon as possible")

    query = update.callback_query
    if update.callback_query.data == '6': query.edit_message_text(text="Selected option: 1")
    elif update.callback_query.data == '7': query.edit_message_text(text="Hello. Please write your inquiry to bookings@erasmusu.com and one agent will get in touch with you as soon as possible")
    elif update.callback_query.data == '8': query.edit_message_text(text="Hello. Please write your inquiry to bookings@erasmusu.com and one agent will get in touch with you as soon as possible")
    elif update.callback_query.data == '9': query.edit_message_text(text="Hello. Please write your inquiry to info@erasmusu.com and one agent will get in touch with you as soon as possible")
    elif update.callback_query.data == '10': query.edit_message_text(text="Hello. Please write your inquiry to info@erasmusu.com and one agent will get in touch with you as soon as possible")



def help(update, context):
    """
    Help function.
    This displays a set of commands available for the bot.
    """
    user = update.message.from_user
    logger.info("User {} asked for help.".format(user.first_name))
    update.message.reply_text("Texto de ayuda",
                              reply_markup=ReplyKeyboardRemove())
@app.route('/')

def main():
    """
    Main function.
    This function handles the conversation flow by setting
    states on each step of the flow. Each state has its own
    handler for the interaction with the user.
    """
    global LANG
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("754596163:AAHdVWjKq1jzVd05YQx60V3qHbyLC7GFCYo", use_context=True)

    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('menu', menu))


    # Get the dispatcher to register handlers:
    dp = updater.dispatcher

    # Add conversation handler with predefined states:
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            SET_LANG: [MessageHandler(Filters.regex('^(ES|EN)$'), set_lang)],

        },

        fallbacks=[CommandHandler('help', help)]
    )

    dp.add_handler(conv_handler)


    # Start DisAtBot:
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process
    # receives SIGINT, SIGTERM or SIGABRT:
    updater.idle()


if __name__ == '__main__':  
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
