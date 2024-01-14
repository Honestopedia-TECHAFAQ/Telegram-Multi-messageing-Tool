import streamlit as st
from telegram.bot import Bot  
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
bot = Bot(token='YOUR_BOT_TOKEN')

def send_message(chat_id, message_content):
    bot.send_message(chat_id=chat_id, text=message_content)

def main():
    st.title("Telegram Bot GUI")
    st.sidebar.header("Options")
    target_chat_id = st.sidebar.text_input("Enter Target Chat ID:", "")
    st.subheader("Send Message")
    message_content = st.text_area("Enter Message:", "")

    if st.button("Send Message"):
        if target_chat_id and message_content:
            send_message(target_chat_id, message_content)
            st.success("Message sent successfully!")
        else:
            st.error("Please provide both Target Chat ID and Message Content.")

if __name__ == '__main__':
    main()
