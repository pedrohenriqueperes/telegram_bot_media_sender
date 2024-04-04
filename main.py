import os
import telebot
from time import sleep
from credencials import *


channel_id = media
folder_to_post = folder
bot = telebot.TeleBot(bot_api)

def send_media_files(folder_path, channel_id, bot):
    """
    Itera pelos arquivos de mídia em uma pasta e os envia para um canal do Telegram em ordem alfabética.
    """
    file_list = os.listdir(folder_path)
    file_list.sort()  # Ordena a lista alfabeticamente

    for filename in file_list:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):  # Verifica se é um arquivo (não um subdiretório)
            try:
                with open(file_path, 'rb') as f:
                    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                        bot.send_photo(channel_id, f)
                        print('sent')
                        sleep(1)  # Pausa de 1 segundo

                    elif filename.lower().endswith('.mp4'):
                        bot.send_video(channel_id, f)
                        print('sent')
                        sleep(1)  # Pausa de 1 segundo

                    elif filename.lower().endswith(('.gif', '.webp')):
                        bot.send_document(channel_id, f)
                        print('sent')
                        sleep(1)  # Pausa de 1 segundo

                    os.remove(file_path)  # Deleta o arquivo após enviar com sucesso

            except Exception as e:
                print(f"Erro ao enviar {filename}: {str(e)}")

            #sleep(10)  # Pausa de 10 segundos entre envios

if __name__ == "__main__":
    while True:
        file_list = os.listdir(folder_to_post)
        if not file_list:
            print("Diretório vazio. Aguardando 15 segundos antes de verificar novamente.")
            sleep(15)  # Pausa de 15 segundos antes de verificar novamente
        else:
            send_media_files(folder_to_post, channel_id, bot)
