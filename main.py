import os
import telebot
from time import sleep

channel_id = int(input('Channel ID: '))
folder_to_post = str(input("Provide Folder Path containing the photos: "))
bot_api = str(input("Insert Bot Api Keys: "))
bot = telebot.TeleBot(bot_api)  

def send_media_files(folder_path, channel_id, bot):
    """
    Iterates through media files in a folder and sends them to a Telegram channel in alphabetical order.

    Args:
        folder_path (str): The path to the folder containing the media files.
        channel_id (str): The Telegram channel ID to send messages to.
        bot (TeleBot): Your initialized TeleBot object.
    """

    file_list = os.listdir(folder_path)
    file_list.sort()  # Sort the list alphabetically

    for filename in file_list:
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):  # Check if it's a file (not a subdirectory)
            try:
                with open(file_path, 'rb') as f:
                    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                        bot.send_photo(channel_id, f)


                    elif filename.lower().endswith('.mp4'):
                        bot.send_video(channel_id, f)


                    elif filename.lower().endswith(('.gif', '.webp')):
                        bot.send_document(channel_id, f)


                    os.remove(file_path)  # Delete the file after successful sending

            except Exception as e:
                print(f"Error sending {filename}: {str(e)}")

            sleep(10)  # Delay 10 seconds

if __name__ == "__main__":
    while True:
        file_list = os.listdir(folder_to_post)
        if not file_list:
            break
        else:
            send_media_files(folder_to_post, channel_id, bot)
