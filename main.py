import random

import telebot
import json
import os
import time

import src.shared
from src.logger import logger, cleanup_old_logs

bot = telebot.TeleBot(src.shared.BOT_TOKEN)
telebot.apihelper.proxy = {
    "https": src.shared.SOCKS5_PROXY_URL,
    "http": src.shared.SOCKS5_PROXY_URL
} if src.shared.SOCKS5_PROXY_URL and src.shared.SOCKS5_PROXY_URL.startswith("socks") else {}


def append_downloaded(sticker_id: str):
    with open("downloaded.txt", "a", encoding="utf-8") as dw:
        dw.write(f"{sticker_id}\n")


def save_sticker_metadata(sticker_set: telebot.types.StickerSet):
    json_data = json.dumps(vars(sticker_set), default=str, indent=None)
    with open("metadata.jsonl", "a", encoding="utf-8") as mt:
        mt.write(json_data + "\n")


def safe_divide(x0: float, x1: float) -> float:
    try:
        return x0 / x1
    except ZeroDivisionError:
        return 0


def download_stickers(file_path: str = "stickers_list.txt"):
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} not found")
        return

    if not os.path.exists("downloads"):
        os.makedirs("downloads", exist_ok=True)

    if not os.path.exists("downloaded.txt"):
        with open('downloaded.txt', 'w', encoding="utf-8") as fp:
            fp.write("")

    if not os.path.exists("metadata.jsonl"):
        with open('metadata.jsonl', 'w', encoding="utf-8") as fp:
            fp.write("")

    with open(file_path, "r") as f:
        sticker_names = {line.strip() for line in f}

    with open("downloaded.txt", "r", encoding="utf-8") as dp:
        downloaded_names = {line.strip() for line in dp}

    for name in sticker_names:
        if name in downloaded_names:
            continue

        os.makedirs(f"downloads/{name}", exist_ok=True)

        try:
            sticker_set = bot.get_sticker_set(name)
            sticker_length = len(sticker_set.stickers)
            logger.info(f"Processing sticker pack: {name}")

            for index, sticker in enumerate(sticker_set.stickers):
                logger.info(f"Saving #{index+1}/#{sticker_length} of '{sticker.set_name}'... ({safe_divide(index + 1, sticker_length):.2%})")
                file_info = bot.get_file(sticker.file_id)
                downloaded_file = bot.download_file(file_info.file_path)

                ext = file_info.file_path.split('.')[-1]
                save_path = f"downloads/{name}/{sticker.file_id}.{ext}"

                with open(save_path, "wb") as s_file:
                    s_file.write(downloaded_file)

                time.sleep(random.uniform(0.6, 1))

            append_downloaded(name)
            save_sticker_metadata(sticker_set)

        except Exception as e:
            logger.error(f"Failed to process {name}: {e}")

    time.sleep(random.uniform(1, 2.5))


if __name__ == "__main__":
    cleanup_old_logs(days=14)
    download_stickers()

    logger.info("Done! :)")
