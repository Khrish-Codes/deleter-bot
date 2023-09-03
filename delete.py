from pyrogram import Client, Filters

# Replace with your bot token
API_TOKEN = "6028376714:AAF_S5pCavnAzUjDqtEGNucoOKPKIuI0KEw"

# Replace with the owner's user ID (integer, not a username)
OWNER_USER_ID = 6408116706

# Create a Pyrogram client
app = Client("my_bot", bot_token=API_TOKEN)


# Function to delete messages in a channel
def delete_channel_messages(client, chat_id):
    messages = client.iter_history(chat_id)
    for message in messages:
        # Check if the message is not from the bot owner
        if message.from_user and message.from_user.id != OWNER_USER_ID:
            message.delete()


# Define a command to start the bot
@app.on_message(Filters.command("start") & Filters.private)
def start(client, message):
    message.reply_text("Bot is now running. It will delete upcoming messages in the channel.")


# Run the bot
if __name__ == "__main__":
    with app:
        app.run()
