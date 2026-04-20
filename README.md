# stickerboom

Telegram bot-based tool to download sticker packs by names listed in a file.

## Setup

### Using pip

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate.bat    # Windows CMD
# or
venv\Scripts\activate.ps1   # Windows PowerShell

pip install "pytelegrambotapi>=4.33.0,<5.0.0" "python-dotenv>=1.2.2,<2.0.0" "requests[socks]>=2.33.1,<3.0.0"
```

## Configuration

Copy `.env-example` to `.env` and fill in your credentials:

```bash
cp .env-example .env  # Linux/macOS
# or
copy .env-example .env   # Windows
```

Edit `.env` with your bot token and optional proxy:

```env
BOT_TOKEN=your_telegram_bot_token_here
# Optional: SOCKS5 proxy
SOCKS5_PROXY_URL=socks5://user:pass@host:port
```

## Usage

1. Create `stickers_list.txt` with sticker pack names, one per line:
```
tea_stickers
cool_stickers_pack
```

2. Run the script:
  ```bash
python main.py
```

3. Outputs:
   - `downloads/` - downloaded sticker files
   - `metadata.jsonl` - metadata for each downloaded pack (one JSON per line)
   - `downloaded.txt` - list of successfully downloaded pack names

The script skips packs already listed in `downloaded.txt`.