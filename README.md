# Telegram Media Sender

## Overview

This Python script automates the process of sending media files (photos, videos, and documents) from a specified folder to a Telegram channel. It also deletes the files after successful sending to prevent duplicates.

## Key Features

- Sends various media types: photos (.jpg, .jpeg, .png), videos (.mp4), and documents (.gif, .webp)
Not working to well for big video files.
- Continuously monitors the folder for new files and sends them automatically
- Deletes files after successful sending
- Sends files in alphabetical order by filename
- Includes a 10-second delay between sending files

## Installation and Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   

2. **Create a Telegram bot:**
   - Contact the BotFather on Telegram to create a new bot and obtain its API token.

3. **Obtain channel ID:**
   - Open the Telegram channel you want to send files to and note its ID (found in the channel's URL).

4. **Configure the script:**
   - Edit the following variables in the `telegram_media_sender.py` file:
     - `channel_id`: Replace with your channel ID.
     - `folder_to_post`: Replace with the path to the folder containing your media files.
     - `bot_token`: Replace with your bot's API token.

## Usage

1. Run the script:
   bash
   python telegram_media_sender.py
   

2. The script will start monitoring the specified folder and send any new media files to the Telegram channel.

## Additional Notes

- **Timeout:** The script includes a 1-hour timeout to prevent indefinite running. Adjust this duration in the code if needed.
- **Error handling:** The script includes basic error handling, but consider enhancing it for specific scenarios.
- **Security:** If handling sensitive information, ensure appropriate security measures are in place.


